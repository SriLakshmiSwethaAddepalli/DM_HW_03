# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering techniques excel in managing outliers compared to k-means, as these outliers often remain isolated or amalgamate towards the end of the clustering sequence. This trait renders outliers more detectable and simpler to exclude."

    # For question (b)"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Applying k-means on the identical dataset multiple instances might lead to different clustering outcomes, while agglomerative hierarchical clustering techniques guarantee uniform clustering results with each run, barring any equality in the proximity measures."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means clustering isn't always quicker or more memory-efficient compared to agglomerative hierarchical clustering, and it's not recognized as the top performer in clustering algorithms. Despite k-means being computationally advantageous, there are algorithms with greater efficiency, such as the leader algorithm, available."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "In the subsequent phase of refining K-means outcomes, the act of dividing a group by designating one member as a fresh center and redistributing members between the initial and the new centers often results in a higher SSE (Sum of Squared Errors) due to the enhanced spread of members relative to their centers."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In the context of k-means clustering, a reduction in SSE (Sum of Squared Errors) signifies enhanced unity within clusters, seeing that SSE inversely reflects the tightness of cluster formation. Therefore, a lower SSE points to clusters being denser and more uniformly integrated."

    # For question (f)
    answers["(f)"] = True  # True if the statement is correct"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "Within k-means clustering, a rise in SSB (Sum of Squares Between clusters) signals greater distinction among clusters, as SSB directly quantifies the degree of separation between them. Consequently, an augmentation in SSB leads to clusters that are more clearly delineated and apart from one another."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In K-Means clustering, cohesion and separation are interlinked concepts. Enhancing cohesion by lowering SSE (Sum of Squared Errors) inherently bolsters separation, evidenced by a rise in SSB (Sum of Squares Between clusters), due to the fact that SSE and SSB are components of the constant total sum of squares (TSS). This means that any improvement in cluster tightness or cohesion simultaneously leads to clearer delineation or separation among clusters."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In the process of k-means clustering, the combined value of SSE (Within Sum of Squares) and SSB (Between Sum of Squares) is a constant, since the overall sum of squares (TSS) does not change during the clustering operation. This relationship is encapsulated by the equation TSS = SSE + SSB, highlighting the direct linkage between internal cluster cohesion, external cluster separation, and the total variance within the data."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "In k-means clustering, reducing SSE (enhancing cohesion) leads to an increase in SSB (improving separation), due to SSE's inverse link with cohesion and SSB's direct connection to separation."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Each shaded sphere hosts a solitary cluster centroid within its midst, given the considerable separation between clusters, precluding any centroid from capturing points from a different cluster."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "In each of the two shaded areas, a single cluster centroid will be positioned at the core. However, the ultimate clusters will encompass points from both shaded zones, due to their proximity and non-circular configuration."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The ultimate outcome of the k-means clustering will include an empty cluster, as the centroid located at 12.5 is more distant from all points compared to other clusters, resulting in it being unoccupied."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10*R**2"
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
    answers["(a) explain"] = "Every point within circle A will align with the centroid inside A. Approximately one third of the points in circle B, specifically those in its leftmost third, will adhere to the leftmost centroid in B. The other two-thirds of B's points, along with all points in circle C, will gravitate towards the centroid at B's heart. This dynamic will shift the rightmost centroid in B towards circle C, due to C's denser point population. In the subsequent iteration, points in circles A, B, and C will realign with centroids situated within their respective circles, leading to the stabilization and convergence of the K-means algorithm."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Due to the nearness of circles A and B and their substantial distance from circle C, points from A and B will cluster around the centroid in A. Circle C's points will be evenly divided among its two centroids, with each holding 50,000 points. The centroid in A will shift between A and B, given their equal point counts. The centroids in C will move slightly but remain within C, each managing half of C's points."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Due to the proximity of circles A and B and their significant distance from circle C, points from A and B will cluster at the centroid in A. Circle C's points will be equally divided between its two centroids, each receiving 50,000 points. With A and B hosting an equal number of points, the centroid in A will oscillate between them. Meanwhile, the centroids within C will slightly separate but remain in C, each with half of C’s points."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A' , 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Combining clusters A and B due to their minimal single-link distance, which signifies their closest points are in near vicinity."

    # type: set
    answers["(b)"] = {'Group A' , 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Joining clusters A and C owing to the smallest complete-link distance between them, highlighting maximum similarity among their most distant points."

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
    answers["(a) explain"] = "Cluster 4 shows the greatest entropy in clustering, indicating a wider variety in types of land cover."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 exhibits the lowest entropy in clustering, due to its prevalent water land cover type and limited diversity."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Each diagonal element is crisply outlined and largely blue, denoting significant internal cluster cohesion. This consistency indicates that points within each cluster are compactly assembled, preserving uniform cluster integrity."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Rows 1 and 3 are attributed to clusters A and C, respectively, discerned by the noticeable color fluctuations in the off-diagonal elements, indicating varying proximities between cluster A (or C) and all other clusters. Rows 2 and 4 correspond to clusters B and D, respectively, illustrating comparable observations."

    # type: string
    answers["(a) Matrix 2"] = "X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Remarkably, two diagonal elements emerge with striking clarity, predominantly adorned in a rich blue hue compared to their counterparts. This distinction underscores the robust unity within clusters B and C, emphasizing the reinforced connections among the constituent elements within these clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows 1 and 4, with less distinct diagonal entries, portray an array of varied colors, depicting varying degrees of proximity to all other clusters. Conversely, rows with clearer diagonal elements exhibit two uniform colors (apart from the diagonal), indicating similar distances to two clusters while maintaining a greater separation from another cluster."

    # type: string
    answers["(a) Matrix 3"] = "Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Resembling the pattern observed in Matrix 2, two diagonal entries stand out with heightened clarity and a deep blue hue, indicating strong cohesion within clusters B and C. This uniformity suggests a more pronounced intra-cluster connectivity within these specific clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "In every row, two off-diagonal entries exhibit matching colors, while the third differs, showcasing that each cluster sustains closer proximity to two other clusters compared to the remaining one. This pattern underscores the unique inter-cluster dynamics and relationships."

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The initial row represents Cluster A. The diagonal element shows a less prominent presence, suggesting a relatively subdued cohesion within this particular cluster. Additionally, all off-diagonal entries showcase an array of distinct colors, indicating diverse degrees of separation from neighboring clusters. Cluster A demonstrates its closest adjacency to Cluster B, succeeded by Cluster C, while maintaining the farthest distance from Cluster D."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The second row is linked with Cluster B. The diagonal element stands out with increased clarity, implying robust internal cohesion within this cluster. Additionally, two out of the three off-diagonal elements share a similar color, suggesting equidistant associations with Clusters A and C, albeit with a slightly less defined proximity to Cluster A. Cluster B is notably distanced from Cluster D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The third row is attributed to Cluster C. The diagonal element stands out with increased prominence, indicating robust intra-cluster cohesion. Moreover, two out of the three off-diagonal elements share identical colors, suggesting equidistant connections with Clusters B and D, albeit with a slightly less distinct proximity to Cluster D. Cluster C demonstrates the greatest separation from Cluster A."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Row 4 corresponds to Cluster D. Similar to Cluster A, the diagonal entry appears less prominent, suggesting weaker cohesion within the cluster. Each off-diagonal entry displays a distinct color, indicating varying degrees of separation from neighboring clusters. Cluster D is nearest to Cluster C, followed by Cluster B, and farthest from Cluster A."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["Hierarchical", "Overlapping", "Complete"]

    # type: list
    answers["(b)"] = ["Partitional", "Exclusive", "Complete"]

    # type: list
    answers["(c)"] = ["Partitional", "Fuzzy", "Complete"]

    # type: list
    answers["(d)"] = ["Hierarchical", "Overlapping", "Partial"]

    # type: list
    answers["(e)"] = ["Partitional", "Exclusive", "Partial"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "The Computer Science department organizes students based on their achievements in the data mining course. This classification follows partitional and exclusive clustering principles, guaranteeing distinct and mutually exclusive categories for each student's grade. However, the clustering is partial since not all students may have participated in the data mining course, leaving some without assignment to any grade category."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "DBSCAN struggles to accurately detect patterns in the presence of excessive noise density."

    # type: string
    answers["(a) Figure (b)"] = "DBSCAN excels at identifying patterns characterized by higher density in contrast to noise."

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The suitability of DBSCAN depends on the distribution of data density."

    # type: string
    answers["(b) Figure (a)"] = "The uniform density assumption of K-means limits its effectiveness in segmenting facial features accurately."

    # type: string
    answers["(b) Figure (b)"] = "With an appropriate number of clusters, K-means can segment facial features effectively, although it may inadvertently include background points."

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The suitability of K-means hinges on the assumption of distinct clusters within the data."

    # type: string
    answers["(c)"] = "Spectral clustering, Gaussian mixture models, or Reciprocal density-based DBSCAN are capable of accurately segmenting facial features presented in Figure (a)."

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
