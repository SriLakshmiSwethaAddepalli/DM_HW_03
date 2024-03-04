# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering methods are more adept at handling outliers compared to k-means because outliers tend to remain as separate clusters or merge late in the clustering process, making them easier to identify and eliminate."

    # For question (b)"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Different runs of k-means on the same dataset may produce different clusterings, whereas agglomerative hierarchical clustering methods will always yield the same clustering unless there are ties in the proximity values."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means clustering is not necessarily faster or less memory-intensive than agglomerative hierarchical clustering, and it is not considered the most efficient clustering algorithm overall. While k-means is computationally efficient, there are more efficient algorithms available, such as the leader algorithm."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "During a post-processing step for K-means, when a cluster is split by selecting one of its points as a new centroid and reassigning points to either the original centroid or the new centroid, the SSE (Sum of Squared Errors) typically increases because splitting increases the dispersion of points from centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In k-means clustering, a decrease in SSE (Sum of Squared Errors) indicates an increase in cohesion, as SSE is an inverse measure of cluster cohesion. Thus, when SSE decreases, clusters become more compact and internally cohesive."

    # For question (f)
    answers["(f)"] = True  # True if the statement is correct"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In k-means clustering, an increase in SSB (the between sum of squares) indicates an increase in separation, as SSB is a direct measure of cluster separation. Therefore, when SSB increases, clusters become more distinct and separated from each other."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Cohesion and separation are not independent in K-Means clustering. Improving cohesion (reducing SSE) necessarily improves separation (increasing SSB), as both SSE and SSB are interconnected through the constant total sum of squares (TSS)."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In k-means clustering, the sum of SSE (Within Sum of Squares) and BSS (Between Sum of Squares) remains constant, as the total sum of squares (TSS) remains constant throughout the clustering process. This relationship is expressed by TSS = SSE + SSB."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "In k-means clustering, an increase in cohesion (reduction in SSE) leads to an increase in separation (increase in SSB). This is because SSE is inversely related to cluster cohesion, while SSB is directly related to cluster separation."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Each shaded circle will have one cluster centroid at its center because the clusters are too far apart for one centroid to attract points from another."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "There will be one cluster centroid in the center of each of the two shaded regions, but the final clusters will consist of points from both shaded regions since they are close to each other and not of circular shape."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The final clustering for k-means contains an empty cluster because the centroid at 12.5 is farther away from all points than any other clusters and will become empty."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "5*R**2"
    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "All of circle A’s points will be assigned to the centroid in A. About ⅓ of circle B’s points (the ones in the left third of circle B) will be assigned to the centroid on the left in circle B. The remaining ⅔ of the points in B and all the points in C will be assigned to the centroid in the center of B. This will cause the right centroid in B to move to circle C since C has many more points.  In the next iteration, all points in A,B, and C will be assigned to the centroids located in their own circles and K-means will converge."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since circles A and B are close together and quite far away from circle C, the points from both A and B will be assigned to the centroid that is in A. The points in C will be split between the two centroids in C, with each centroid having 50,000 points. Since A and B have the same number of points each, the centroid in A will move between A and B. The centroids in C will move apart slightly but both will remain in C, each having half of C’s points."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since circles A and B are close together and quite far away from circle C, the points from both A and B will be assigned to the centroid that is in A. The points in C will be split between the two centroids in C, with each centroid having 50,000 points. Since A and B have the same number of points each, the centroid in A will move between A and B. The centroids in C will move apart slightly but both will remain in C, each having half of C’s points."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A' , 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Merging groups A and B because they have the smallest single link distance, indicating close proximity in their nearest points."

    # type: set
    answers["(b)"] = {'Group A' , 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Merging groups A and C because they have the smallest complete link distance, indicating the greatest similarity between their furthest points."

    return answers





# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B', 'C', 'D', 'E', 'F', 'G'}

    # type: set
    answers["(b) cluster 2"] = {'I', 'J', 'L', 'M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M', 'D', 'G'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 exhibits the largest clustering entropy due to higher variability in land cover types."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 shows the smallest clustering entropy attributed to its dominant representation of water land cover and minimal variability."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Each diagonal entry appears sharply defined and predominantly blue, indicating strong cohesion within clusters. This uniformity suggests that points within a given cluster are closely grouped together, maintaining consistent cluster coherence"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Rows 1 and 3 correspond to clusters A and C, respectively, based on the distinct color variations in the off-diagonal entries, indicating varying distances between cluster A (or C) and all other clusters. Rows 2 and 4 align with clusters B and D, respectively, reflecting similar observations"

    # type: string
    answers["(a) Matrix 2"] = "X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Notably, two diagonal entries are notably crisp and predominantly blue compared to the others, signifying superior cohesion within clusters B and C. This distinction underscores tighter intra-cluster relationships within these clusters"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows with less defined diagonal entries (rows 1 and 4) exhibit a range of distinct colors, reflecting varying distances from all other clusters. Conversely, rows with sharper diagonal entries display two identical colors (apart from the diagonal), indicating equidistant relationships with two clusters while maintaining a greater distance from one cluster"

    # type: string
    answers["(a) Matrix 3"] = "Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Similar to Matrix 2, two diagonal entries display heightened clarity and blue intensity, denoting robust cohesion within clusters B and C. This consistency implies stronger intra-cluster relationships within these clusters"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Each row displays two similarly colored off-diagonal entries and one distinct color, indicating that each cluster maintains relatively closer proximity to two other clusters compared to the remaining one, highlighting distinct inter-cluster relationships"

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Row 1 represents Cluster A. The diagonal entry appears less distinct, indicating relatively weaker cohesion within this cluster. Additionally, all off-diagonal entries display varying colors, implying diverse distances from other clusters. Cluster A is closest to Cluster B, followed by Cluster C, and farthest from Cluster D."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Row 2 corresponds to Cluster B. The diagonal entry appears more pronounced, suggesting strong intra-cluster cohesion. Furthermore, two out of three off-diagonal entries share the same color, indicating equidistant relationships with Clusters A and C, although the proximity to Cluster A is slightly less defined. Cluster B exhibits the greatest distance from Cluster D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Row 3 corresponds to Cluster C. The diagonal entry appears more pronounced, suggesting strong intra-cluster cohesion. Furthermore, two out of three off-diagonal entries share the same color, indicating equidistant relationships with Clusters B and D, although the proximity to Cluster D is slightly less defined. Cluster C exhibits the greatest distance from Cluster A."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Row 4 corresponds to Cluster D. Similar to Cluster A, the diagonal entry appears less distinct, implying lower cohesion within the cluster. All off-diagonal entries exhibit different colors, indicating varying distances from other clusters. Cluster D is closest to Cluster C, followed by Cluster B, and farthest from Cluster A."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["Hierarchical", "Overlapping", "Partial"]

    # type: list
    answers["(b)"] = ["Partitional", "Exclusive", "Complete"]

    # type: list
    answers["(c)"] = ["Partitional", "Fuzzy", "Complete"]

    # type: list
    answers["(d)"] = ["Hierarchical", "Overlapping", "Partial"]

    # type: list
    answers["(e)"] = ["Partitional", "Exclusive", "Partial"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "students in the Computer Science department are grouped based on their grades in the data mining class. This follows partitional and exclusive clustering principles, ensuring distinct and non-overlapping categories for each student's grade. However, the clustering is partial because not all students may have taken the data mining class, leaving some unassigned to any grade category"

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "DBSCAN cannot effectively identify patterns due to high noise density."

    # type: string
    answers["(a) Figure (b)"] = "DBSCAN can identify patterns as they have higher density compared to noise."

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN suitability based on density distribution."

    # type: string
    answers["(b) Figure (a)"] = "K-means cannot effectively segment facial features due to uniform density assumption."

    # type: string
    answers["(b) Figure (b)"] = "K-means can segment facial features with a proper number of clusters, but may include background points."

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means suitability based on cluster assumption."

    # type: string
    answers["(c)"] = "spectral clustering or Gaussian mixture models or Reciprocal density-based DBSCAN can effectively segment facial features in Figure (a)."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
