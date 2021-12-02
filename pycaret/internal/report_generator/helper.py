# report helper

# Specific to model type
def get_plot_list(model_name, model_type):
    plot_list = ''
    if model_type == 'regression':
        plot_list = ['residuals', 'error', 'cooks', 'rfe', 'learning', 'manifold', 'feature', 'feature_all',
                     'parameter', 'tree', 'vc']
    elif model_type == 'classification':
        plot_list = ['auc', 'pr', 'confusion_matrix', 'error', 'class_report', 'boundary', 'learning', 'vc',
                     'dimension', 'feature', 'feature_all']
    elif model_type == 'clustering':
        plot_list = ['cluster', 'tsne', 'elbow', 'silhouette', 'distance', 'distribution']
    elif model_type == 'anomaly_detection':
        plot_list == ['tsne', 'umap']
    elif model_type == 'nlp':
        plot_list = ['frequency', 'distribution', 'bigram', 'trigram', 'sentiment', 'tsne', 'topic_distribution',
                     'wordcloud']
    return plot_list


def get_model_definition(model_name, model_type):
    model_definition = ''
    if model_type == 'regression':
        model_definition = get_model_definition_regression(model_name)
    elif model_type == 'classification':
        model_definition = get_model_definition_classification(model_name)
    elif model_type == 'clustering':
        model_definition = get_model_definition_clustering(model_name)
    elif model_type == 'anomaly_detection':
        model_definition == get_model_definition_anomaly_detection(model_name)
    elif model_type == 'nlp':
        model_definition = get_model_definition_nlp(model_type)
    return model_definition


def get_model_definition_regression(model_name):
    model_name_dict = {
        'lr': 'Linear regression model with a single explanatory variable.It concerns two-dimensional sample points '
              'with one independent variable and one dependent variableand finds a linear function that, '
              'as accurately as possible, predicts the dependent variable values as a function of the independent '
              'variable. It fits a linear model with coefficients w = (w1, …, wp) to minimize the residual sum of '
              'squares between the observed targets in the dataset, and the targets predicted by the linear '
              'approximation.',
        'lasso': 'Lasso regression is a type of linear regression that uses shrinkage. Shrinkage is where data values '
                 'are shrunk towards a central point, like the mean. The lasso procedure encourages simple, '
                 'sparse models (i.e. models with fewer parameters). This particular type of regression is '
                 'well-suited for models showing high levels of muticollinearity or when you want to automate certain '
                 'parts of model selection, like variable selection/parameter elimination.',
        'ridge': 'Ridge regression addresses some of the problems of Ordinary Least Squares by imposing a penalty on '
                 'the size of the coefficients. Ridge regression is a way to create a parsimonious model when the '
                 'number of predictor variables in a set exceeds the number of observations, or when a data set has '
                 'multicollinearity (correlations between predictor variables).The ridge coefficients minimize a '
                 'penalized residual sum of squares.',
        'en': 'The elastic net method performs variable selection and regularization simultaneously. The elastic net '
              'technique is most appropriate where the dimensional data is greater than the number of samples used. '
              'Groupings and variables selection are the key roles of the elastic net technique.',
        'lar': 'Least-angle regression (LARS) is an algorithm for fitting linear regression models to '
               'high-dimensional data, developed by Bradley Efron, Trevor Hastie, Iain Johnstone and Robert '
               'Tibshirani. Suppose we expect a response variable to be determined by a linear combination of a '
               'subset of potential covariates. Then the LARS algorithm provides a means of producing an estimate of '
               'which variables to include, as well as their coefficients.Instead of giving a vector result, '
               'the LARS solution consists of a curve denoting the solution for each value of the L1 norm of the '
               'parameter vector. The algorithm is similar to forward stepwise regression, but instead of including '
               'variables at each step, the estimated parameters are increased in a direction equiangular to each '
               'correlations with the residual.',
        'llar': 'Least-angle regression (LARS) is an algorithm for fitting linear regression models to '
                'high-dimensional data, developed by Bradley Efron, Trevor Hastie, Iain Johnstone and Robert '
                'Tibshirani. Suppose we expect a response variable to be determined by a linear combination of a '
                'subset of potential covariates. Then the LARS algorithm provides a means of producing an estimate of '
                'which variables to include, as well as their coefficients.Instead of giving a vector result, '
                'the LARS solution consists of a curve denoting the solution for each value of the L1 norm of the '
                'parameter vector. The algorithm is similar to forward stepwise regression, but instead of including '
                'variables at each step, the estimated parameters are increased in a direction equiangular to each '
                'correlations with the residual.',
        'omp': 'The orthogonal matching pursuit (OMP) or orthogonal greedy algorithm is more complicated than MP. The '
               'OMP starts the search by finding a column of A with maximum correlation with measurements y at the '
               'first step and thereafter at each iteration it searches for the column of A with maximum correlation '
               'with the current residual. In each iteration, the estimation of the signal vector is updated by the '
               'highly correlated column of A .',
        'br': 'Bayesian regression allows a natural mechanism to survive insufficient data or poorly distributed data '
              'by formulating linear regression using probability distributors rather than point estimates. The '
              'output or response ‘y’ is assumed to drawn from a probability distribution rather than estimated as a '
              'single value.One of the most useful type of Bayesian regression is Bayesian Ridge regression which '
              'estimates a probabilistic model of the regression problem.',
        'ard': 'Automatic relevance determination (ARD), and the closely-related sparse Bayesian learning (SBL) '
               'framework, are effective tools for pruning large numbers of irrelevant features. However, '
               'popular update rules used for this process are either prohibitively slow in practice and/or heuristic '
               'in nature without proven convergence properties. This paper furnishes an alternative means of '
               'optimizing a general ARD cost function using an auxiliary function that can naturally be solved using '
               'a series of re-weighted L1 problems. The result is an efficient algorithm that can be implemented '
               'using standard convex programming toolboxes and is guaranteed to converge to a stationary point '
               'unlike existing methods. The analysis also leads to additional insights into the behavior of previous '
               'ARD updates as well as the ARD cost function. For example, the standard fixed-point updates of MacKay '
               '(1992) are shown to be iteratively solving a particular min-max problem, although they are not '
               'guaranteed to lead to a stationary point. The analysis also reveals that ARD is exactly equivalent to '
               'performing MAP estimation using a particular feature- and noise-dependent \textit{non-factorial} '
               'weight prior with several desirable properties over conventional priors with respect to feature '
               'selection. In particular, it provides a tighter approximation to the L0 quasi-norm sparsity measure '
               'than the L1 norm. Overall these results suggests alternative cost functions and update procedures for '
               'selecting features and promoting sparse solutions.',
        'par': 'Passive-Aggressive algorithms are generally used for large-scale learning. It is one of the few '
               '‘online-learning algorithms‘. In online machine learning algorithms, the input data comes in '
               'sequential order and the machine learning model is updated step-by-step, as opposed to batch '
               'learning, where the entire training dataset is used at once. This is very useful in situations where '
               'there is a huge amount of data and it is computationally infeasible to train the entire dataset '
               'because of the sheer size of the data. We can simply say that an online-learning algorithm will get a '
               'training example, update the classifier, and then throw away the example.',
        'ransac': 'Random sample consensus (RANSAC) is an iterative method to estimate parameters of a mathematical '
                  'model from a set of observed data that contains outliers, when outliers are to be accorded no '
                  'influence on the values of the estimates. Therefore, it also can be interpreted as an outlier '
                  'detection method.[1] It is a non-deterministic algorithm in the sense that it produces a '
                  'reasonable result only with a certain probability, with this probability increasing as more '
                  'iterations are allowed. The algorithm was first published by Fischler and Bolles at SRI '
                  'International in 1981. They used RANSAC to solve the Location Determination Problem (LDP), '
                  'where the goal is to determine the points in the space that project onto an image into a set of '
                  'landmarks with known locations. RANSAC uses repeated random sub-sampling.[2] A basic assumption is '
                  'that the data consists of "inliers", i.e., data whose distribution can be explained by some set of '
                  'model parameters, though may be subject to noise, and "outliers" which are data that do not fit '
                  'the model. The outliers can come, for example, from extreme values of the noise or from erroneous '
                  'measurements or incorrect hypotheses about the interpretation of data. RANSAC also assumes that, '
                  'given a (usually small) set of inliers, there exists a procedure which can estimate the parameters '
                  'of a model that optimally explains or fits this data.',
        'tr': 'In non-parametric statistics, the Theil–Sen estimator is a method for robustly fitting a line to '
              'sample points in the plane (simple linear regression) by choosing the median of the slopes of all '
              'lines through pairs of points. It has also been called Sen slope estimator,slope selection, '
              'the single median method, the Kendall robust line-fit method, and the Kendall–Theil robust line. It is '
              'named after Henri Theil and Pranab K. Sen, who published papers on this method in 1950 and 1968 '
              'respectively,[8] and after Maurice Kendall because of its relation to the Kendall tau rank correlation '
              'coefficient. This estimator can be computed efficiently, and is insensitive to outliers. It can be '
              'significantly more accurate than non-robust simple linear regression (least squares) for skewed and '
              'heteroskedastic data, and competes well against least squares even for normally distributed data in '
              'terms of statistical power.[10] It has been called "the most popular nonparametric technique for '
              'estimating a linear trend".',
        'huber': 'Huber Regressor is a linear regression model that is robust to outliers.The Huber Regressor '
                 'optimizes the squared loss for the samples where |(y - Xw)/ sigma| < epsilon and the absolute loss '
                 'for the samples where |(y - Xw) / sigma| > epsilon, where w and sigma are parameters to be '
                 'optimized. The parameter sigma makes sure that if y is scaled up or down by a certain factor, '
                 'one does not need to rescale epsilon to achieve the same robustness. Note that this does not take '
                 'into account the fact that the different features of X may be of different scales.This makes sure '
                 'that the loss function is not heavily influenced by the outliers while not completely ignoring '
                 'their effect.',
        'kr': 'Kernel ridge regression (KRR) combines Ridge regression and classification (linear least squares with '
              'l2-norm regularization) with the kernel trick. It thus learns a linear function in the space induced '
              'by the respective kernel and the data. For non-linear kernels, this corresponds to a non-linear '
              'function in the original space.The form of the model learned by KernelRidge is identical to support '
              'vector regression (SVR). However, different loss functions are used: KRR uses squared error loss while '
              'support vector regression uses -insensitive loss, both combined with l2 regularization. In contrast to '
              'SVR, fitting KernelRidge can be done in closed-form and is typically faster for medium-sized datasets. '
              'On the other hand, the learned model is non-sparse and thus slower than SVR, which learns a sparse '
              'model  at prediction-time.',
        'svm': 'Support-vector machines (SVMs, also support-vector networks) are supervised learning models with '
               'associated learning algorithms that analyze data for classification and regression analysis. '
               'Developed at AT&T Bell Laboratories by Vladimir Vapnik with colleagues (Boser et al., 1992, '
               'Guyon et al., 1993, Vapnik et al., 1997[citation needed]) SVMs are one of the most robust prediction '
               'methods, being based on statistical learning frameworks or VC theory proposed by Vapnik (1982, '
               '1995) and Chervonenkis (1974). Given a set of training examples, each marked as belonging to one of '
               'two categories, an SVM training algorithm builds a model that assigns new examples to one category or '
               'the other, making it a non-probabilistic binary linear classifier (although methods such as Platt '
               'scaling exist to use SVM in a probabilistic classification setting). SVM maps training examples to '
               'points in space so as to maximise the width of the gap between the two categories. New examples are '
               'then mapped into that same space and predicted to belong to a category based on which side of the gap '
               'they fall.In addition to performing linear classification, SVMs can efficiently perform a non-linear '
               'classification using what is called the kernel trick, implicitly mapping their inputs into '
               'high-dimensional feature spaces.When data are unlabelled, supervised learning is not possible, '
               'and an unsupervised learning approach is required, which attempts to find natural clustering of the '
               'data to groups, and then map new data to these formed groups. The support-vector clustering '
               'algorithm, created by Hava Siegelmann and Vladimir Vapnik, applies the statistics of support vectors, '
               'developed in the support vector machines algorithm, to categorize unlabeled data, and is one of the '
               'most widely used clustering algorithms in industrial applications.',
        'knn': 'The k-nearest neighbors algorithm (k-NN) is a non-parametric classification method first developed by '
               'Evelyn Fix and Joseph Hodges in 1951,and later expanded by Thomas Cover.It is used for classification '
               'and regression. In both cases, the input consists of the k closest training examples in a data set. '
               'The output depends on whether k-NN is used for classification or regression.In k-NN classification, '
               'the output is a class membership. An object is classified by a plurality vote of its neighbors, '
               'with the object being assigned to the class most common among its k nearest neighbors (k is a '
               'positive integer, typically small). If k = 1, then the object is simply assigned to the class of that '
               'single nearest neighbor.In k-NN regression, the output is the property value for the object. This '
               'value is the average of the values of k nearest neighbors.k-NN is a type of classification where the '
               'function is only approximated locally and all computation is deferred until function evaluation. '
               'Since this algorithm relies on distance for classification, if the features represent different '
               'physical units or come in vastly different scales then normalizing the training data can improve its '
               'accuracy dramatically.Both for classification and regression, a useful technique can be to assign '
               'weights to the contributions of the neighbors, so that the nearer neighbors contribute more to the '
               'average than the more distant ones. For example, a common weighting scheme consists in giving each '
               'neighbor a weight of 1/d, where d is the distance to the neighbor.The neighbors are taken from a set '
               'of objects for which the class (for k-NN classification) or the object property value (for k-NN '
               'regression) is known. This can be thought of as the training set for the algorithm, though no '
               'explicit training step is required.A peculiarity of the k-NN algorithm is that it is sensitive to the '
               'local structure of the data.',
        'dt': 'Decision tree learning or induction of decision trees is one of the predictive modelling approaches '
              'used in statistics, data mining and machine learning. It uses a decision tree (as a predictive model) '
              'to go from observations about an item (represented in the branches) to conclusions about thetarget '
              'value (represented in the leaves). Tree models where the target variable can take a discrete set of '
              'values are called classification trees; in these tree structures, leaves represent class labels and '
              'branches represent conjunctions of features that lead to those class labels. Decision trees where the '
              'target variable can take continuous values (typically real numbers) are called regression trees. '
              'Decision trees are among the most popular machine learning algorithms given their intelligibility and '
              'simplicity.In decision analysis, a decision tree can be used to visually and explicitly represent '
              'decisions and decision making. In data mining, a decision tree describes data (but the resulting '
              'classification tree can be an input for decision making). This page deals with decision trees in data '
              'mining.Along with classification,Decision trees can also be applied to regression problems.',
        'rf': 'Random forests or random decision forests are an ensemble learning method for classification, '
              'regression and other tasks that operates by constructing a multitude of decision trees at training '
              'time. For classification tasks, the output of the random forest is the class selected by most trees. '
              'For regression tasks, the mean or average prediction of the individual trees is returned.Random '
              'decision forests correct for decision trees habit of overfitting to their training set.Random forests '
              'generally outperform decision trees, but their accuracy is lower than gradient boosted trees. However, '
              'data characteristics can affect their performance.The first algorithm for random decision forests was '
              'created in 1995 by Tin Kam Ho using the random subspace method, which is a way to implement the '
              '"stochastic discrimination" approach to classification proposed by Eugene Kleinberg.An extension of '
              'the algorithm was developed by Leo Breiman and Adele Cutler,who registered "Random Forests" as a '
              'trademark in 2006 (as of 2019, owned by Minitab, Inc.). The extension combines Breiman "bagging" idea '
              'and random selection of features, introduced first by Ho and later independently by Amit and Geman in '
              'order to construct a collection of decision trees with controlled variance.Random forests are '
              'frequently used as blackbox models in businesses, as they generate reasonable predictions across a '
              'wide range of data while requiring little configuration.',
        'et': 'A meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various '
              'sub-samples of the dataset and uses averaging to improve the predictive accuracy and control '
              'over-fitting.',
        'ada': 'The core principle of AdaBoost is to fit a sequence of weak learners (i.e., models that are only '
               'slightly better than random guessing, such as small decision trees) on repeatedly modified versions '
               'of the data. The predictions from all of them are then combined through a weighted majority vote (or '
               'sum) to produce the final prediction. The data modifications at each so-called boosting iteration '
               'consist of applying weights to each of the training samples. Initially, those weights are all set so '
               'that the first step simply trains a weak learner on the original data. For each successive iteration, '
               'the sample weights are individually modified and the learning algorithm is reapplied to the '
               'reweighted data. At a given step, those training examples that were incorrectly predicted by the '
               'boosted model induced at the previous step have their weights increased, whereas the weights are '
               'decreased for those that were predicted correctly. As iterations proceed, examples that are difficult '
               'to predict receive ever-increasing influence. Each subsequent weak learner is thereby forced to '
               'concentrate on the examples that are missed by the previous ones in the sequence.',
        'gbr': 'Gradient boosting is a machine learning technique for regression, classification and other tasks, '
               'which produces a prediction model in the form of an ensemble of weak prediction models, '
               'typically decision trees.When a decision tree is the weak learner, the resulting algorithm is called '
               'gradient boosted trees, which usually outperforms random forest.It builds the model in a stage-wise '
               'fashion like other boosting methods do, and it generalizes them by allowing optimization of an '
               'arbitrary differentiable loss function.',
        'mlp': 'A multilayer perceptron (MLP) is a class of feedforward artificial neural network (ANN). The term MLP '
               'is used ambiguously, sometimes loosely to mean any feedforward ANN, sometimes strictly to refer to '
               'networks composed of multiple layers of perceptrons (with threshold activation). Multilayer '
               'perceptrons are sometimes colloquially referred to as "vanilla" neural networks, especially when they '
               'have a single hidden layer.An MLP consists of at least three layers of nodes: an input layer, '
               'a hidden layer and an output layer. Except for the input nodes, each node is a neuron that uses a '
               'nonlinear activation function. MLP utilizes a supervised learning technique called backpropagation '
               'for training.Its multiple layers and non-linear activation distinguish MLP from a linear perceptron. '
               'It can distinguish data that is not linearly separable.',
        'xgboost': 'XGBoost is an open-source software library which provides a regularizing gradient boosting '
                   'framework. It aims to provide a scalable, portable and distributed gradient boosting (GBM, GBRT, '
                   'GBDT) library". It runs on a single machine, as well as the distributed processing frameworks '
                   'Apache Hadoop, Apache Spark, Apache Flins, and Dask.',
        'lightgbm': 'Gradient boosting is a machine learning technique for regression, classification and other '
                    'tasks, which produces a prediction model in the form of an ensemble of weak prediction models, '
                    'typically decision trees.When a decision tree is the weak learner, the resulting algorithm is '
                    'called gradient boosted trees, which usually outperforms random forest.It builds the model in a '
                    'stage-wise fashion like other boosting methods do, and it generalizes them by allowing '
                    'optimization of an arbitrary differentiable loss function.',
        'catboost': 'CatBoost is an algorithm for gradient boosting on decision trees. It is developed by Yandex '
                    'researchers and engineers, and is used for search, recommendation systems, personal assistant, '
                    'self-driving cars, weather prediction and many other tasks at Yandex and in other companies, '
                    'including CERN, Cloudflare, Careem taxi. '
    }
    return model_name_dict[model_name]


def get_model_definition_classification(model_name):
    model_name_dict = {
        'lr': 'Linear regression model with a single explanatory variable.It concerns two-dimensional sample points '
              'with one independent variable and one dependent variableand finds a linear function that, '
              'as accurately as possible, predicts the dependent variable values as a function of the independent '
              'variable. It fits a linear model with coefficients w = (w1, …, wp) to minimize the residual sum of '
              'squares between the observed targets in the dataset, and the targets predicted by the linear '
              'approximation.',
        'knn': 'The k-nearest neighbors algorithm (k-NN) is a non-parametric classification method first developed by '
               'Evelyn Fix and Joseph Hodges in 1951,and later expanded by Thomas Cover.It is used for classification '
               'and regression. In both cases, the input consists of the k closest training examples in a data set. '
               'The output depends on whether k-NN is used for classification or regression.In k-NN classification, '
               'the output is a class membership. An object is classified by a plurality vote of its neighbors, '
               'with the object being assigned to the class most common among its k nearest neighbors (k is a '
               'positive integer, typically small). If k = 1, then the object is simply assigned to the class of that '
               'single nearest neighbor.In k-NN regression, the output is the property value for the object. This '
               'value is the average of the values of k nearest neighbors.k-NN is a type of classification where the '
               'function is only approximated locally and all computation is deferred until function evaluation. '
               'Since this algorithm relies on distance for classification, if the features represent different '
               'physical units or come in vastly different scales then normalizing the training data can improve its '
               'accuracy dramatically.Both for classification and regression, a useful technique can be to assign '
               'weights to the contributions of the neighbors, so that the nearer neighbors contribute more to the '
               'average than the more distant ones. For example, a common weighting scheme consists in giving each '
               'neighbor a weight of 1/d, where d is the distance to the neighbor.The neighbors are taken from a set '
               'of objects for which the class (for k-NN classification) or the object property value (for k-NN '
               'regression) is known. This can be thought of as the training set for the algorithm, though no '
               'explicit training step is required.A peculiarity of the k-NN algorithm is that it is sensitive to the '
               'local structure of the data.',
        'nb': 'A Naive Bayes classifier is a probabilistic machine learning model that’s used for classification task. The crux of the classifier is based on the Bayes theorem.Using Bayes theorem, we can find the probability of A happening, given that B has occurred. Here, B is the evidence and A is the hypothesis. The assumption made here is that the predictors/features are independent. That is presence of one particular feature does not affect the other. Hence it is called naive.',
        'dt': 'Decision Tree Classifier is a simple and widely used classification technique. It applies a straitforward idea to solve the classification problem. Decision Tree Classifier poses a series of carefully crafted questions about the attributes of the test record. Each time time it receive an answer, a follow-up question is asked until a conclusion about the calss label of the record is reached.',
        'svm': 'It is the most basic type of kernel, usually one dimensional in nature. It proves to be the best function when there are lots of features. The linear kernel is mostly preferred for text-classification problems as most of these kinds of classification problems can be linearly separated.',
        'rbfsvm': 'It is one of the most preferred and used kernel functions in svm. It is usually chosen for non-linear data. It helps to make proper separation when there is no prior knowledge of data.',
        'gpc': 'Gaussian Processes are a generalization of the Gaussian probability distribution and can be used as the basis for sophisticated non-parametric machine learning algorithms for classification and regression.',
        'mlp': 'MLPClassifier trains iteratively since at each time step the partial derivatives of the loss function with respect to the model parameters are computed to update the parameters.It can also have a regularization term added to the loss function that shrinks model parameters to prevent overfitting.',
        'ridge': ' The Ridge Classifier,  based on Ridge regression method, converts the label data into [-1, 1] and solves the problem with regression method. The highest value in prediction is accepted as a target class and for multiclass data muilti-output regression is applied.',
        'rf':'A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.',
        'qda': 'Quadratic Discriminant Analysis (QDA) is a generative model. QDA assumes that each class follow a Gaussian distribution. The class-specific prior is simply the proportion of data points that belong to the class. The class-specific mean vector is the average of the input variables that belong to the class.',
        'ada': "An AdaBoost [1] classifier is a meta-estimator that begins by fitting a classifier on the original dataset and then fits additional copies of the classifier on the same dataset but where the weights of incorrectly classified instances are adjusted such that subsequent classifiers focus more on difficult cases.",
        'gbc': "Gradient Boosting for classification.Gradient Boosting builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage n_classes_ regression trees are fit on the negative gradient of the binomial or multinomial deviance loss function. Binary classification is a special case where only a single regression tree is induced.",
        'lda': 'Linear discriminant analysis (LDA), normal discriminant analysis (NDA), or discriminant function analysis is a generalization of Fishers linear discriminant, a method used in statistics and other fields, to find a linear combination of features that characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier, or, more commonly, for dimensionality reduction before later classification.',
        'et':"An extra-trees classifier.This class implements a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.",
        'xgboost': "Gradient boosting is a machine learning technique for regression and classification problems, which produces a prediction model in the form of an ensemble of weak prediction models, typically decision trees. It builds the model in a stage-wise fashion like other boosting methods do, and it generalizes them by allowing optimization of an arbitrary differentiable loss function.XGBoost is one of the implementations of Gradient Boosting concept, but what makes XGBoost unique is that it uses “a more regularized model formalization to control over-fitting, which gives it better performance,” according to the author of the algorithm, Tianqi Chen. Therefore, it helps to reduce overfitting.",
        'lightgbm': "Light Gradient Boosted Machine, or LightGBM for short, is an open-source library that provides an efficient and effective implementation of the gradient boosting algorithm.LightGBM extends the gradient boosting algorithm by adding a type of automatic feature selection as well as focusing on boosting examples with larger gradients. This can result in a dramatic speedup of training and improved predictive performance.",
        "catboost":'CatBoost is a recently open-sourced machine learning algorithm from Yandex. It can easily integrate with deep learning frameworks like Google’s TensorFlow and Apple’s Core ML. It can work with diverse data types to help solve a wide range of problems that businesses face today. To top it up, it provides best-in-class accuracy'


    }
    return model_name_dict[model_name]


def get_model_definition_clustering(model_name):
    model_name_dict = {
        'kmeans': 'K-means clustering is one of the simplest and popular unsupervised machine '
                  'learning algorithms.A cluster refers to a collection of data points aggregated '
                  'together because of certain similarities.Define a target number k, which refers '
                  'to the number of centroids you need in the dataset. A centroid is the imaginary '
                  'or real location representing the center of the cluster.Every data point is '
                  'allocated to each of the clusters through reducing the in-cluster sum of '
                  'squares.In other words, the K-means algorithm identifies k number of centroids, '
                  'and then allocates every data point to the nearest cluster, while keeping the '
                  'centroids as small as possible.The ‘means’ in the K-means refers to averaging of '
                  'the data; that is, finding the centroid.',
        'ap': 'Affinity propagation (AP) is a clustering algorithm based on the concept of "message '
              'passing" between data points.[1] Unlike clustering algorithms such as k-means or '
              'k-medoids, affinity propagation does not require the number of clusters to be '
              'determined or estimated before running the algorithm. Similar to k-medoids, '
              'affinity propagation finds "exemplars," members of the input set that are '
              'representative of clusters.',
        'meanshift': 'Meanshift is falling under the category of a clustering algorithm in contrast '
                     'of Unsupervised learning that assigns the data points to the clusters '
                     'iteratively by shifting points towards the mode (mode is the highest density '
                     'of data points in the region, in the context of the Meanshift). As such, '
                     'it is also known as the Mode-seeking algorithm. Mean-shift algorithm has '
                     'applications in the field of image processing and computer vision.Unlike the '
                     'popular K-Means cluster algorithm, mean-shift does not require specifying the '
                     'number of clusters in advance. The number of clusters is determined by the '
                     'algorithm with respect to the data.Mean-shift builds upon the concept of '
                     'kernel density estimation is sort KDE. Imagine that the above data was '
                     'sampled from a probability distribution. KDE is a method to estimate the '
                     'underlying distribution also called the probability density function for a '
                     'set of data.It works by placing a kernel on each point in the data set. A '
                     'kernel is a fancy mathematical word for a weighting function generally used '
                     'in convolution. There are many different types of kernels, but the most '
                     'popular one is the Gaussian kernel. Adding up all of the individual kernels '
                     'generates a probability surface example density function. Depending on the '
                     'kernel bandwidth parameter used, the resultant density function will vary.',
        'sc': 'In multivariate statistics, spectral clustering techniques make use of the spectrum '
              '(eigenvalues) of the similarity matrix of the data to perform dimensionality '
              'reduction before clustering in fewer dimensions. The similarity matrix is provided '
              'as an input and consists of a quantitative assessment of the relative similarity of '
              'each pair of points in the dataset.In application to image segmentation, '
              'spectral clustering is known as segmentation-based object categorization.',
        'hclust': 'The agglomerative clustering is the most common type of hierarchical clustering '
                  'used to group objects in clusters based on their similarity. It’s also known as '
                  'AGNES (Agglomerative Nesting). The algorithm starts by treating each object as a '
                  'singleton cluster. Next, pairs of clusters are successively merged until all '
                  'clusters have been merged into one big cluster containing all objects. The '
                  'result is a tree-based representation of the objects, '
                  'named dendrogram.Agglomerative clustering works in a “bottom-up” manner. That '
                  'is, each object is initially considered as a single-element cluster (leaf). At '
                  'each step of the algorithm, the two clusters that are the most similar are '
                  'combined into a new bigger cluster (nodes). This procedure is iterated until all '
                  'points are member of just one single big cluster (root) (see figure below).The '
                  'inverse of agglomerative clustering is divisive clustering, which is also known '
                  'as DIANA (Divise Analysis) and it works in a “top-down” manner. It begins with '
                  'the root, in which all objects are included in a single cluster. At each step of '
                  'iteration, the most heterogeneous cluster is divided into two. ',
        'dbscan': '',
        'optics': 'Ordering points to identify the clustering structure (OPTICS) is an algorithm '
                  'for finding density-based clusters in spatial data. It was presented by Mihael '
                  'Ankerst, Markus M. Breunig, Hans-Peter Kriegel and Jörg Sander.Its basic idea is '
                  'similar to DBSCAN, but it addresses one of DBSCANs major weaknesses: the problem '
                  'of detecting meaningful clusters in data of varying density.To do so, '
                  'the points of the database are(linearly) ordered such that spatially closest '
                  'points become neighbors in the ordering.Additionally, a special distance is '
                  'stored for each point that represents the density that must be accepted for a '
                  'cluster so that both points belong to the same cluster.This is represented as a '
                  'dendrogram.',
        'birch': 'BIRCH (balanced iterative reducing and clustering using hierarchies) is an '
                 'unsupervised data mining algorithm used to perform hierarchical clustering over '
                 'particularly large data-sets. With modifications it can also be used to '
                 'accelerate k-means clustering and Gaussian mixture modeling with the '
                 'expectation–maximization algorithm.An advantage of BIRCH is its ability to '
                 'incrementally and dynamically cluster incoming, multi-dimensional metric data '
                 'points in an attempt to produce the best quality clustering for a given set of '
                 'resources (memory and time constraints). In most cases, BIRCH only requires a '
                 'single scan of the database.Its inventors claim BIRCH to be the "first clustering '
                 'algorithm proposed in the database area to handle noise (data points that are not '
                 'part of the underlying pattern) effectively, beating DBSCAN by two months. The '
                 'BIRCH algorithm received the SIGMOD 10 year test of time award in 2006.',
        'kmodes': ''
    }
    return model_name_dict[model_name]


def get_model_definition_anomaly_detection(model_name):
    model_name_dict = {
        'abod': 'Angle-based Outlier Detection (ABOD) evaluates the degree of outlierness on the variance of the '
                'angles (VOA) between a point and all other pairs of points in the data set.The smaller the angle '
                'variance of the point has,the more likely it is an outlier.',
        'cluster': '',
        'cof': '',
        'histogram': '',
        'knn': '',
        'lof': 'The Local Outlier Factor (LOF) algorithm is an unsupervised anomaly detection method which computes '
               'the local density deviation of a given data point with respect to its neighbors. It considers as '
               'outliers the samples that have a substantially lower density than their neighbors. This example '
               'shows how to use LOF for novelty detection. Note that when LOF is used for novelty detection you '
               'MUST not use predict, decision_function and score_samples on the training set as this would lead to '
               'wrong results. You must only use these methods on new unseen data (which are not in the training '
               'set). See User Guide: for details on the difference between outlier detection and novelty detection '
               'and how to use LOF for outlier detection.The number of neighbors considered, (parameter n_neighbors) '
               'is typically set 1) greater than the minimum number of samples a cluster has to contain, '
               'so that other samples can be local outliers relative to this cluster, and 2) smaller than the '
               'maximum number of close by samples that can potentially be local outliers. In practice, '
               'such information is generally not available, and taking n_neighbors=20 appears to work well in '
               'general.',
        'svm': '',
        'pca': 'The principal components of a collection of points in a real coordinate space are a sequence of  '
               'unit vectors, where the i-th vector is the direction of a line that best fits the data while being '
               'orthogonal to the first i-1 vectors. Here, a best-fitting line is defined as one that minimizes the '
               'average squared distance from the points to the line. These directions constitute an orthonormal '
               'basis in which different individual dimensions of the data are linearly uncorrelated. Principal '
               'component analysis (PCA) is the process of computing the principal components and using them to '
               'perform a change of basis on the data, sometimes using only the first few principal components and '
               'ignoring the rest.PCA is used in exploratory data analysis and for making predictive models. It is '
               'commonly used for dimensionality reduction by projecting each data point onto only the first few '
               'principal components to obtain lower-dimensional data while preserving as much of the data variation '
               'as possible. The first principal component can equivalently be defined as a direction that maximizes '
               'the variance of the projected data. The i-th principal component can be taken as a direction '
               'orthogonal to the first i-1 principal components that maximizes the variance of the projected '
               'data.From either objective, it can be shown that the principal components are eigenvectors of the '
               'data covariance matrix. Thus, the principal components are often computed by eigen decomposition of '
               'the data covariance matrix or singular value decomposition of the data matrix. PCA is the simplest '
               'of the true eigenvector-based multivariate analyses and is closely related to factor analysis. '
               'Factor analysis typically incorporates more domain specific assumptions about the underlying '
               'structure and solves eigenvectors of a slightly different matrix. PCA is also related to canonical '
               'correlation analysis (CCA). CCA defines coordinate systems that optimally describe the '
               'cross-covariance between two datasets while PCA defines a new orthogonal coordinate system that '
               'optimally describes variance in a single dataset.Robust and L1-norm-based variants of standard PCA '
               'have also been proposed.',
        'mcd': 'The minimum covariance determinant (MCD) estimator is one of the first affine equivariant and highly '
               'robust estimators of multivariate location and scatter.1,2 Being resistant to outlying observations,'
               'makes the MCD very helpful in outlier detection.Although already introduced in 1984, its main use '
               'has only started since the introduction of the computationally efficient FAST-MCD algorithm of '
               'Rousseeuw and Van Driessen.Since then, the MCD has been applied in numerous fields such as medicine, '
               'finance, image analysis, and chemistry. Moreover, the MCD has also been used to develop many robust '
               'multivariate techniques, such as principal component analysis, factor analysis, and multiple '
               'regression.',
        'sod': 'Rare data in a large-scale database are called outliers that reveal significant information in the '
               'real world. The subspace-based outlier detection is regarded as a feasible approach in very high '
               'dimensional space. However, the outliers found in subspaces are only part of the true outliers in '
               'high dimensional space, indeed. The outliers hidden in normal-clustered points are sometimes '
               'neglected in the projected dimensional subspace. In this paper, we propose a robust subspace method '
               'for detecting such inner outliers in a given dataset, which uses two dimensional-projections: '
               'detecting outliers in subspaces with local density ratio in the first projected dimensions; finding '
               'outliers by comparing neighbors positions in the second projected dimensions. Each points weight is '
               'calculated by summing up all related values got in the two steps projected dimensions, and then the '
               'points scoring the largest weight values are taken as outliers. By taking a series of experiments '
               'with the number of dimensions from 10 to 10000, the results show that our proposed method achieves '
               'high precision in the case of extremely high dimensional space, and works well in low dimensional '
               'space.',
        'sos': 'Stochastic Outlier Selection is an unsupervised outlier-selection algorithm that takes as input '
               'either a feature matrix or a dissimilarity matrix and outputs for each data point an outlier '
               'probability. Intuitively, a data point is considered to be an outlier when the other data points '
               'have insufficient affinity with it.'
    }
    return model_name_dict[model_name]


def get_model_definition_nlp(model_name):
    model_name_dict = {
        'lda ': 'In natural language processing, the latent Dirichlet allocation (LDA) is a generative statistical '
                'model that allows sets of observations to be explained by unobserved groups that explain why some '
                'parts of the data are similar. For example, if observations are words collected into documents, '
                'it posits that each document is a mixture of a small number of topics and that each words presence '
                'is attributable to one of the documents topics. LDA is an example of a topic model and belongs to '
                'the machine learning field and in a wider sense to the artificial intelligence field.',
        'lsi ': 'Latent Semantic Indexing, also known as latent semantic analysis, is a mathematical practice that '
                'helps classify and retrieve information on particular key terms and concepts using singular value '
                'decomposition (SVD).Through SVD, search engines are able to scan through unstructured data and '
                'identify any relationships between these terms and their context to better index these records for '
                'users online.',
        'hdp ': 'In statistics and machine learning, the hierarchical Dirichlet process (HDP) is a nonparametric '
                'Bayesian approach to clustering grouped data.It uses a Dirichlet process for each group of data, '
                'with the Dirichlet processes for all groups sharing a base distribution which is itself drawn from a '
                'Dirichlet process. This method allows groups to share statistical strength via sharing of clusters '
                'across groups. The base distribution being drawn from a Dirichlet process is important, '
                'because draws from a Dirichlet process are atomic probability measures, and the atoms will appear in '
                'all group-level Dirichlet processes. Since each atom corresponds to a cluster, clusters are shared '
                'across all groups.',
        'rp ': 'Random projection is a technique used to reduce the dimensionality of a set of points which lie in '
               'Euclidean space. Random projection methods are known for their power, simplicity, and low error rates '
               'when compared to other methods. According to experimental results, random projection preserves '
               'distances well, but empirical results are sparse.They have been applied to many natural language '
               'tasks under the name random indexing.',
        'nmf ': 'Non-negative matrix factorization (NMF or NNMF), also non-negative matrix approximation is a group '
                'of algorithms in multivariate analysis and linear algebra where a matrix V is factorized into ('
                'usually) two matrices W and H, with the property that all three matrices have no negative elements. '
                'This non-negativity makes the resulting matrices easier to inspect. Also, in applications such as '
                'processing of audio spectrograms or muscular activity, non-negativity is inherent to the data being '
                'considered. Since the problem is not exactly solvable in general, it is commonly approximated '
                'numerically.'
    }
    return model_name_dict[model_name]


def get_plot_name(plot):
    plot_dict = {
        'auc': ' Area Under the Curve',
        'threshold': ' Discrimination Threshold',
        'pr': ' Precision Recall Curve',
        'confusion_matrix': ' Confusion Matrix',
        'error': ' Prediction Error Plot',
        'class_report': ' Classification Report',
        'boundary': ' Decision Boundary',
        'rfe': ' Recursive Feature Selection',
        'learning': ' Learning Curve',
        'manifold': ' Manifold Learning',
        'calibration': ' Calibration Curve',
        'vc': ' Validation Curve',
        'dimension': ' Dimension Learning',
        'feature': ' Feature Importance',
        'feature_all': ' Feature Importance (All)',
        'parameter': ' Model Hyperparameter',
        'lift': ' Lift Curve',
        'gain': ' Gain Chart',
        'tree': ' Decision Tree',
        'ks': ' KS Statistic Plot',
        'residuals': ' Residuals Plot',
        'cooks': ' Cooks Distance Plot',
        'cluster': ' Cluster PCA Plot (2d)',
        'elbow': ' Elbow Plot',
        'silhouette': ' Silhouette Plot',
        'distance': ' Distance Plot',
        'distribution': 'Distribution Plot',
        'tsne': ' t - SNE (3d) Dimension Plot',
        'frequency': 'Word Token Frequency ',
        'bigram': 'Bigram Frequency Plot ',
        'trigram': 'Trigram Frequency Plot ',
        'sentiment': 'Sentiment Polarity Plot ',
        'pos': 'Part of Speech Frequency ',
        'topic_model': 'Topic Model (pyLDAvis) ',
        'topic_distribution': 'Topic Infer Distribution ',
        'wordcloud': 'Word Cloud ',
        'umap': 'UMAP Dimensionality Plot '
    }
    return plot_dict[plot]


def get_plot_definition(plot):
    plot_definition = {
        'auc': 'Area under the curve is calculated by different methods, of which the antiderivative method of '
               'finding the area is most popular. The area under the curve can be found by knowing the equation of '
               'the curve, the boundaries of the curve, and the axis enclosing the curve. ',
        'threshold': 'The discrimination threshold is the probability or score at which the positive class is chosen '
                     'over the negative class. Generally, this is set to 50% but the threshold can be adjusted to '
                     'increase or decrease the sensitivity to false positives or to other application factors.',
        'pr': 'The precision-recall curve shows the tradeoff between precision and recall for different threshold. A '
              'high area under the curve represents both high recall and high precision, where high precision '
              'relates to a low false positive rate, and high recall relates to a low false negative rate. High '
              'scores for both show that the classifier is returning accurate results (high precision), as well as '
              'returning a majority of all positive results (high recall).',
        'confusion_matrix': 'A confusion matrix is a table that is often used to describe the performance of a '
                            'classification model (or "classifier") on a set of test data for which the true values '
                            'are known.',
        'error': 'The class prediction error chart provides a way to quickly understand how good your classifier is '
                 'at predicting the right classes.',
        'class_report': 'A classification report is a performance evaluation metric in machine learning. It is used '
                        'to show the precision, recall, F1 Score, and support of your trained classification model.',
        'boundary': 'A decision boundary is the region of a problem space in which the output label of a classifier '
                    'is ambiguous. If the decision surface is a hyperplane, then the classification problem is '
                    'linear, and the classes are linearly separable. Decision boundaries are not always clear cut.',
        'rfe': 'Recursive feature elimination (RFE) is a feature selection method that fits a model and removes the '
               'weakest feature (or features) until the specified number of features is reached',
        'learning': 'A learning curve is a plot of model learning performance over experience or time. Learning '
                    'curves are a widely used diagnostic tool in machine learning for algorithms that learn from a '
                    'training dataset incrementally.',
        'manifold': 'A manifold curve is a generalization and abstraction of the notion of a curved surface.',
        'calibration': 'Calibration curves are used to evaluate how calibrated a classifier is i.e., how the '
                       'probabilities of predicting each class label differ. The x-axis represents the average '
                       'predicted probability in each bin. The y-axis is the ratio of positives (the proportion of '
                       'positive predictions).',
        'vc': 'A Validation Curve is an important diagnostic tool that shows the sensitivity between to changes in a '
              'model’s accuracy with change in some parameter of the model. A validation curve is typically drawn '
              'between some parameter of the model and the model’s score. Two curves are present in a validation '
              'curve – one for the training set score and one for the cross-validation score. By default, '
              'the function for validation curve, present in the scikit-learn library performs 3-fold '
              'cross-validation. A validation curve is used to evaluate an existing model based on hyper-parameters '
              'and is not used to tune a model. This is because, if we tune the model according to the validation '
              'score, the model may be biased towards the specific data against which the model is tuned; thereby, '
              'not being a good estimate of the generalization of the model.',
        'dimension': 'dimension',
        'feature': 'Feature importance refers to techniques that assign a score to input features based on how '
                   'useful they are at predicting a target variable.',
        'feature_all': 'this plot shows the relative importance of all the features for a given dataset.',
        'parameter': 'A model hyperparameter is a configuration that is external to the model and whose value cannot '
                     'be estimated from data.',
        'lift': 'The Lift curve shows the curves for analysing the proportion of true positive data instances in '
                'relation to the classifiers threshold or the number of instances that we classify as positive.',
        'gain': 'The cumulative gains curve is an evaluation curve that assesses the performance of the model and '
                'compares the results with the random pick. It shows the percentage of targets reached when '
                'considering a certain percentage of the population with the highest probability to be target '
                'according to the model.',
        'tree': 'A decision tree is a flowchart-like structure in which each internal node represents a test on an '
                'attribute',
        'ks': 'The KS test report the maximum difference between the two cumulative distributions, and calculates a '
              'P value from that and the sample sizes.',
        'residuals_interactive': 'A residual plot is a type of plot that displays the values of a predictor variable '
                                 'in a regression model along the x-axis and the values of the residuals along the '
                                 'y-axis.',
        'residuals': 'A residual plot is a type of plot that displays the values of a predictor variable in a '
                     'regression model along the x-axis and the values of the residuals along the y-axis.',
        'cooks': 'Cooks Distance is an estimate of the influence of a data point. It takes into account both the '
                 'leverage and residual of each observation. Cooks Distance is a summary of how much a regression '
                 'model changes when the ith observation is removed.',
        'cluster': 'Principal Component Analysis (PCA) is a popular technique for deriving a set of low dimensional '
                   'features from a larget set of variables. However, another popular application of PCA is '
                   'visualizing higher dimensional data. In this tutorial, we will go over the basics of PCA and '
                   'apply it to cluster a data set consisting of houses with different features.',
        'elbow': 'The elbow method plots the value of the cost function produced by different values of k. As you '
                 'know, if k increases, average distortion will decrease, each cluster will have fewer constituent '
                 'instances, and the instances will be closer to their respective centroids.',
        'silhouette': 'The silhouette plot displays a measure of how close each point in one cluster is to points in '
                      'the neighboring clusters and thus provides a way to assess parameters like number of clusters '
                      'visually.',
        'distance': 'A distance-time graph shows how far an object has travelled in a given time.It is a simple line '
                    'graph that denotes distance versus time findings on the graph.',
        'frequency': 'It is a distribution because it tells us how the total number of word tokens in the text are '
                     'distributed across the vocabulary items.',
        'distribution': 'This plot details the distribution of words in a text across the vocabulary items.',
        'bigram': 'A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are '
                  'typically letters, syllables, or words. A bigram is an n-gram for n=2. The frequency distribution '
                  'of every bigram in a string is commonly used for simple statistical analysis of text in many '
                  'applications, including in computational linguistics, cryptography, speech recognition, and so on.',
        'trigram': 'Trigrams are a special case of the n-gram, where n is 3. They are often used in natural language '
                   'processing for performing statistical analysis of texts and in cryptography for control and use '
                   'of ciphers and codes.',
        'sentiment': 'The key aspect of sentiment analysis is to analyze a body of text for understanding the '
                     'opinion expressed by it. Typically, we quantify this sentiment with a positive or negative '
                     'value, called polarity. The overall sentiment is often inferred as positive, neutral or '
                     'negative from the sign of the polarity score',
        'pos': 'The rate of occurrence of anything; the relationship between incidence and time period.',
        'tsne': 'T-SNE is a common visualization for understanding high-dimensional data, and right now the '
                'variable tsne is an array where each row represents a set of (x, y, z) coordinates from the obtained '
                'embedding.',
        'topic_model': 'In machine learning and natural language processing, a topic model is a type of statistical '
                       'model for discovering the abstract "topics" that occur in a collection of documents. Topic '
                       'modeling is a frequently used text-mining tool for discovery of hidden semantic structures in '
                       'a text body. ',
        'topic_distribution': 'Each word in the document is attributed to a particular topic with probability given '
                              'by this distribution. Topics themselves are defined as probability distributions over '
                              'the vocabulary.',
        'wordcloud': 'Word Clouds (also known as wordle, word collage or tag cloud) are visual representations of '
                     'words that give greater prominence to words that appear more frequently',
        'umap': 'UMAP is a nonlinear dimensionality reduction method, it is very effective for visualizing clusters '
                'or groups of data points and their relative proximities.'
    }
    return plot_definition[plot]


def get_image_name(plot):
    image_name_dict = {
        'residuals ': 'Residuals.png',
        'error ': 'Prediction Error.png',
        'cooks ': 'Cooks Distance.png',
        'rfe ': 'Feature Selection.png',
        'learning ': 'Learning Curve.png',
        'vc ': 'Validation Curve.png',
        'manifold ': 'Manifold Learning.png',
        'feature ': 'Feature Importance.png',
        'feature_all ': 'Feature Importance (All).png',
        'parameter ': 'Hyperparameters.png',
        'tree ': 'Decision Tree.png',
        'plotIdentifier': 'Image Name',
        'auc ': 'AUC.png',
        'threshold ': 'Threshold.png',
        'pr ': 'Precision Recall.png',
        'confusion_matrix ': 'Confusion Matrix.png',
        'class_report ': 'Class Report.png',
        'boundary ': ' Decision Boundary.png',
        'calibration ': 'Calibration Curve.png',
        'dimension ': 'Dimensions.png',
        'lift ': 'Lift Chart.png',
        'gain ': 'Gain Chart.png',
        'ks ': 'KS Statistic Plot.png',
        'cluster': 'cluster',
        'elbow': 'Elbow.png',
        'silhouette': 'Silhouette.png',
        'distance': 'Distance.png',
        'tsne ': 'tsne',
        'umap ': 'umap',
        'frequency': 'Word Frequency.html',
        'distribution': 'Distribution.html',
        'bigram': 'Bigram.html',
        'trigram': 'Trigram.html',
        'sentiment': 'Sentiments.html',
        'pos': 'pos.html',
        'tsne': 'TSNE.html',
        'topic_model': '',
        'topic_distribution': 'Topic Distribution.html',
        'wordcloud': 'Wordcloud.png',
        'umap': 'umap'
    }
    return image_name_dict[plot]
