#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:56:48 2021

@author: philippe
"""


books="""
\itemno{{\it The Weighted Bootstrap}, avec Patrice Bertail (INRA), 
{\it Lecture Notes in Statistics}, Fevrier 1995, Springer.}

\itemno{{\it Cours de Probabilit\'e pour la Licence}, avec Michel
Ledoux, 1999, Belin et Editions 31; 2nd edition EDP (2007).}

\itemno{{\it Integral over Asymptotic Sets, with Applications in
Statistics and Probability}, t\'el\'echar\-gea\-ble \`a
{\tt http://xxx.arxiv.org/abs/math.PR/0312132}.}

\itemno{{\it Asymptotic expansions for infinite weighted convolutions
of heavy tail distributions and applications}, avec W.P.\ McCormick), 
{\it Memoirs of the American Mathematical Society}, 2009.}
"""

articles="""

\itemno{Un co\^{u}t du ch\^{o}mage?, {\it Travail et Emploi}, 40, 63-71.}

\itemno{Sur la probabilit\'{e} qu'un cylindre coupe un r\'{e}seau de plans 
dans $\IR^3$, {\it Publication de l'ISUP}, XXIV, Fasc. 3, 3--8 (1989).}

\itemno{Limiting distribution of the maximal spacing when the density
function admits a positive minimum, {\it Statistics and Probability
Letters}, 14, 53--60, 1992.}

\itemno{Weighted approximation of the renewal spacing processes, 
{\it Journal of Multivariate Analysis}, 45, 171--182, 1993.}

\itemno{Limiting distribution of the minimal spacing,
{\it Mathematical Method of Statistics}, 3, 306--325, 1993.}

\itemno{Joint approximation of processes based on spacings and order
 statistics, {\it Stochastic Processes and their Applications}, 53,
 339--349 (1994).}

\itemno{A review on some large deviation results, {\it Publication de
l'ISUP}, XXXVIII, 3--24, 1994.}

\itemno{On the limiting distribution function for the spacings,
{\it Statistics}, 25, 367--373, 1994.}

\itemno{Statistiques de rangs lin\'eaires, normalit\'e asymptotique et
th\'eror\`eme de projection de H\'ajek (with M.\ Hallin), in {\it
Inf\'erence Non Param\'etrique -- Les Statistiques de rangs},
pp.167--202, J.-J. Droesbeke and J. Fine Eds., \'Edition de
l'Universit\'e de Bruxelles and Ellipse.}

\itemno{On Kendall's process (avec Ch.\ Genest, K.\ Ghoudi, B.\
R\'emillard), {\it Journal of Multivariate Analysis}, 58, 197--229, 1996.}

\itemno{Functional Erd\"os-R\'enyi laws for processes indexed by sets
(avec M.\ Broniatowski), {\it Journal of Mathematical Sciences}, 83, 356--369,
1996.}

\itemno{Bootstrapping of the renewal spacing processes, 
{\it Journal of Statistical Planning and Inference}, 60, 199--214, 1997.}

\itemno{Deviation principle for set indexed processes with independent 
increments (avec M.\ Broniatowski), {\it Studia
Scientiarum Mathematicarum Hungarica}, 33, 393--418, 1997.}

\itemno{Statistical Analysis of mixtures and the empirical probability
measure, {\it Acta Applicandae Mathematicae}, 50, 253--340, 1998.}

\itemno{Large deviation principle for sequential rank processes 
(avec M.\ Broniatowski), {\it Mathematical Methods of Statistics},
7, 98--110, 1998}

\itemno{Last passage time for the empirical mean of some mixing processes,
avec M.\ Doisy and B. Garel, {\it Statistics and Probability
Letters}, 40, 237--245, 1998.}

\itemno{Note on functional large deviation principle for fractional ARIMA 
processes, avec M.\ Broniatowski, {\it Statistical Inference
for Stochastic Processes}, 1, 17--27, 1998.}

\itemno{Simulation in exponential families, avec M. Broniatowski,
{\it ACM Transactions on Modeling and Computer Simulation 
(TOMACS), 9, 203--223, 1999.}}

\itemno{Relationship between preparation convergence, retention
and vertical displacement of extracoronal retainers (with D.\
Chan (DMD, MS, DDS) and A.H.\ Wilson (DDS)),
{\it Proceedings of the American Association of Dental Research 2001 
conference}, 
Chicago, IL.}

\itemno{A central limit theorem for rejective sampling}, {\sl Sankhy\`a, A},
65, 1--22, 2003.

\itemno{Effect of preparation convergence on retention and seating 
discrepancy of complete veneer crowns (with D.C.N.\ Chan, A.H.\ Wilson, 
R.J.\ Cronin, C.\ Chung, K.\ Chung), {\it Journal of Oral Rehabilitation}, 31,
1007--1013, 2004.}

\itemno{Blowing number of a distribution for a statistics and loyal estimators
(avec M.\ Broniatowski), {\sl Statistics and Probability Letters},
69, 465--475, 2004.}

\itemno{Second order expansion for the maximum of some stationnary Gaussian 
sequences (avec W.P.\ McCormick) {\sl Stochastic Processes and their 
Applications}, 110, 315--342, 2004.}

\itemno{Tail calculus with remainder, applications to tail expansions for
infinite order moving averages, randomly stopped sums, and related topics
(avec W.P.\ McCormick), {\sl Extremes}, 7, 337--365, 2004.}

\itemno{Asymptotic expansions of convolutions of regularly varying
distributions (avec W.P.\ McCormick), {\sl Journal of Australian
Mathematical Society}, 78, 339--371, 2005.}

\itemno{On sharp large deviations for sums of random vectors and
multidimensional Laplace approximation (avec M.\ Broniatowski), {\sl
Theory of Probability and its Applications}, 49, 561--588, 2005.}

\itemno{On the tail behavior of sums of dependent risks 
(avec A.L.\ Foug\`eres and Ch.\ Genest), {\sl Astin Bulletin}, 36, 361--373,
2006.}

\itemno{Asymptotic expansions for distributions of compound sums of 
random variables with rapidly varying subexponential distribution
(avec W.P.\ McCormick and C.\ Zhang), {\sl Journal of Applied Probability},
670--684, 2007.}

\itemno{Tail expansions for the distribution of the maximum of a random walk
with negative drift and regularly varying increments (avec W.P.\ McCormick and
C.\ Zhang), {\sl Stochastic Processes and their Applications}, 117, 1835--1847,
2007.}

\itemno{Asymptotic expansions for weighted convolutions of light subexponential
distribution (avec W.P.\ McCormick), {\sl Theory of Probability and Related
Fields}, 141, 155--180, 2008.}

\itemno{An extension of a logarithmic form of Cram\'er's ruin theorem to some
FARIMA and related processes (avec W.P.\ McCormick), {\sl Stochastic Processes
and their Applications}, 120, 801--828, 2010.}

\itemno{Veraverbeke's theorem at large: on the maximum of some processes with
negative drift and heavy tail innovations (avec W.P.\ McCormick), {\sl 
Extremes}, 14, 63--125, 2012.}

\itemno{A critical reanalysis of Maryland State Police searches, {\sl The American Statistician}, 66, 1--7, 2012 avec W.C.\ Horrace}

\itemno{Heavy-traffic approximations for fractionally integrated random walks in the domain of attraction of a non-Gaussian stable distribution, {\sl Stochastic Processes and their Applications}, 122, 1276--1303, 2012, 
avec W.P.\ McCormick}

\itemno{The point process approach for fractionally differentiated random walks under heavy traffic, {\sl Stochastic Processes and their Applications}, 122, 4028--4053, 2012, avec W.P.\ McCormick}

\itemno{Invariance principles for some FARIMA and nonstationary linear processes in the domain of a stable distribution, {\sl Probability Theory and Related Fields}, 154, 429--476, 2012, avec W.P.\ McCormick}

"""


unpublished = """

\itemno{Consistent exact tests for semiparametric single-index models (avec
%Fr\'ed\'eric Jouneau-Sion et Oliver Torr\`es).}

\itemno{q-Catalan bases and their dual coefficients, {\tt arXiv:1211.6206}, avec W.P. McCormick, 46 p.}

\itemno{A conditional limit theorem for a bivariate representation of a univariate random variable and conditional extreme values, {\tt arXiv:1311.0540}, avec M.I.\ Seifert, 23 p.}

\itemno{Some Tauberian theory for the $q$-Lagrange inversion, {\tt arXiv:1312.6899}, avec W.P.\ McCormick, 43 p.}


%\smallskip
%\noindent {\bf En pr\'eparation:}

\smallskip
\noindent{\bf Travaux non publi\'es :}

\count1=1
\itemno{Aspect statistique des modes, raport pour le laboratoire de la consommation,
INRA, 1993.}

\itemno{Le co\^{u}t du ch\^{o}mage, Tech. Rep., Minist\`{e}re des
affaires sociales et de l'emploi, SES, 1987.}

\hfuzz=5pt
\itemno{M\'{e}thodes d'estimation de surfaces \`{a} partir d'une image
num\'{e}rique (avec N. Caron, J. Couronne, D. Deschemeaker, C. Jourdren, G. Nicod),
Tech. Rep., Minist\`{e}re de la mer (1989).}

\hfuzz=0pt
\itemno{Estimation non param\'{e}trique de l'entropie et de l'information 
de Kullback, Tech. Rep., CREST (1991).}

\itemno{On q-algebraic equations and their power series solutions, 53 p., {\tt arXiv.1311.5549}, avec W.P.\ McCormick.}

"""

[books, articles, unpublished]