from __future__ import division
from math import sqrt
import re, random 

from django.conf import settings


WIDTH = settings.DC_SVG_WIDTH - 50
HEIGHT = settings.DC_SVG_HEIGHT - 50

STOPWORDS =\
[u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he',\
u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs',\
u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were',\
u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if',\
u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into'\
, u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off',\
u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any',\
u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so',\
u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']


def pearson(vec1,vec2):
    '''
    A simple pearson distance
    the arguments are vec1 and vec2
    '''
    sum1 = sum(vec1)
    sum2 = sum(vec2)

    # sums of the squares
    sum1Sq = sum([pow(v,2) for v in vec1])
    sum2Sq = sum([pow(v,2) for v in vec2])    

    # sum of the products
    pSum = sum([vec1[i]*vec2[i] for i in range(len(vec1))])

    # calculate r (Pearson score)
    num = pSum-(sum1*sum2/len(vec1))
    den = sqrt((sum1Sq-pow(sum1,2)/len(vec1))*(sum2Sq-pow(sum2,2)/len(vec1)))
    if den==0:
        return 0
    return 1.0-num/den


def scaledown(data, distance=pearson, rate=0.01):
    '''
    This function accepts multidimensional data (>2)
    and scales down to 2 dimensions so that the new
    scaled down dimensions can be drawn on 2D surface
    '''
    number_of_blogs = len(data)

    # real distances among various rows/blogs
    realdist = ( [[ distance(data[i], data[j])
        for j in range(number_of_blogs)]
        for i in range(0, number_of_blogs)] )

    # initialize a random location as a starting point on 2D
    loc = [ [random.random(), random.random()] for i in range(number_of_blogs)]
    fake_dist = [[0.0 for j in range(number_of_blogs)] for i in range(number_of_blogs)]

    last_error = None
    for m in range(0, 1000):
        # find projected distances between the points
        for i in range(number_of_blogs):
            for j in range(number_of_blogs):
                fake_dist[i][j] =  sqrt(sum([pow(loc[i][x]-loc[j][x],2) 
                                 for x in range(len(loc[i]))]))
        # move points
        grad = [[0.0, 0.0] for i in range(number_of_blogs)]

        total_error = 0.0
        for k in range(number_of_blogs):
            for j in range(number_of_blogs):
                if j == k:
                    continue
                # error = percentage difference between distances
                error_term =  (fake_dist[j][k]-realdist[j][k])/realdist[j][k]

                # the distance each point needs to be moved towards 
                # or away is directly proportional to the error
                grad[k][0] += ((loc[k][0]-loc[j][0])/fake_dist[j][k]) * error_term
                grad[k][1] += ((loc[k][1]-loc[j][1])/fake_dist[j][k]) * error_term

                # increase the total error
                total_error += abs(error_term)
        print("Total error: {}".format(total_error))

        # stop when the total_error gets worse if points are moved
        if last_error and last_error<total_error:
            break 
        last_error = total_error

        # move each point by learning_rate * gradient (grad)
        for k in range(number_of_blogs):
            loc[k][0] -= rate * grad[k][0] 
            loc[k][1] -= rate * grad[k][1] 

    return loc 


def words_from_html(html):
    '''
    This function parses html and returns an array of words
    '''
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('',html)
    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    # Convert to lowercase
    return [ word.lower() for word in words if word != ''
    and word not in STOPWORDS ]


def normalize(vectors):
    '''
    Normalized vectors
    e.g. [1, 2, 3] should return [0, .5, 1]
    done by using  by (point - min)/(max - min)
    '''
    x_points = [x[0] for x in vectors]
    y_points = [y[1] for y in vectors]

    max_x, min_x = max(x_points), min(x_points)
    max_y, min_y = max(y_points), min(y_points)

    new_points = [[(point[0] - min_x)/(max_x - min_x), (point[1] - min_y)/(max_y - min_y)]
    for point in vectors]

    return new_points


def scale_height_width(scaled_matrix, translate = 50):
    '''
    This scales the extra width and height of scaled 
    2-dimensional points.
    e.g. [200, 300], [2000, 1000] will be scaled to 
    [0 + translate, 0 + translate], [1800 + translate, 700 + translate ]
    '''
    normalized_data = normalize(scaled_matrix)

    scaled_matrix = [[point[0] * WIDTH + translate, point[1] * HEIGHT+translate] 
    for point in normalized_data]

    return scaled_matrix