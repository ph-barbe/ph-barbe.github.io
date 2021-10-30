---
layout: post
title: Documenting large and complex Data Science projects
image: writing-828911_1920.jpg
credit: Image by Free-Photos from Pixabay
---
Search for *best practices for documenting complex Data Science projects* and you although you find many articles and books about how to document Data Science projects, few will address documentation of large, complex Data Science projects.

Because the field is technical, complexity is often understood in technical terms. That is, using an *algorithm* that is complex, or *data* that are complex. With *projects*, complexity is about the scope of the project.

A large project doesn’t involve a few data sets, but many, sometimes very many. Not one model, but very many. Not a single algorithm, but many, some being custom designed, some being possibly new and not part of anyone’s knowledge outside part of the team. Medium size projects can benefit from techniques used in large ones.

A large Data Science project is very much like a large Engineering project, where multiple components need to be integrated. It can involve thousands of files and a large number of people with different skill sets.

When managing a large and complex undertaking how does one communicate to new managers what the project is about? How does one communicate to new team members how they fit into the overall project? How does one grasp the totality of the project, navigate it, and be able to find a single line of code if needed? How does a manager deal with these challenges and still preserve agility?

The standard (small project) advice of documenting using Jupyter notebooks may be *part* of the solution if your project uses notebooks, but it is not the full solution. Indeed, if your project is sizable, notebooks will be a small part of the solution.

Documenting code at the file, function and classes levels is *part* of the solution too but does not give much of a clue about how components interact and seldom give enough context to appreciate how the code will be used.

Many easily accessible good practices work well for small projects, and since a large project is often decomposed into smaller ones, these good practices can be *part* of the solution.

One of my colleagues documented an enterprise effort with a large poster in his office depicting a maze of databases, data pipelines, data processing steps, user interfaces, etc that he had created over a decade as the chief architect of the project. As he walked me through his poster explaining how some components were built and the history behind them it struck me that, with his poster, *he* was the documentation! But there was a *real* documentation in the case of his departure.

## Graphs

In order to be executed, complex projects need to be broken down into sub-projects. The systems that are built are made of subsystems.

A first step is to document that breakdown into subsystems, sub-subsystems and so on.

A graph may express how the different components interact. While we often see simple ones with few components, highly complex ones can be very effective at describing complex systems as long as the logical grouping is clear. I have seen some with several hundred nodes, which clearly communicated business processes that were translated into Data Science and Software Engineering components.

Graphs are also useful to describe complex data pipelines and transformations. By representing databases, data acquisitions systems, transformations, and the flow of information, they depict data sources, logic, and sometimes synchronicity. They may also include information on how people may be involved in data pipelines or data acquisitions, information on costs, bottle necks… Color of nodes, node content, thickness and annotations on edges, all can add useful and easily understood important information.

Regardless of their purpose, large graph layouts have to be well thought out to convey the dependencies, hierarchy and conceptual organization.

## Modeling document

Because there is a current trend in Data Science to emphasize on algorithms instead of the conceptual goals that algorithms try to achieve, models are often documented in terms of the algorithms used.

To understand large projects, the goal of the documentation goes far beyond the specific algorithms used, and in fact the specific algorithms are almost incidental.

Modeling documents for large projects can span several hundreds of pages, organized by subsystems. Their goal is to give a conceptual view on the project as a whole and on each of its parts.

## Entities

At the root are the business entities which need to have some representation using clear terminology.

Proper definitions of even simple terms should be spelled out. What is a customer? What is an order? What is a transaction? Basic things that are taken for granted should be defined.

Not only defining them ensure that everyone knows what they are talking about, but it also forces one to reflect on the entities that appear in the business, and delineate their exact scope. What makes someone a customer? Is it paying for the service offered by company? But what if employees get this service for free? Aren’t they customers?

Try to define what a “table” is and is not. You may be surprised by how much arbitrariness needs to be introduced to properly define this every day object! Am I talking about a database or the physical object in an office on which you do your work?

By asking these questions, exceptions appear, and this forces the team to better understand what the business is doing.

## Mathematical representations

Building mathematical representations of these business entities expresses an opinion on how one should think of these entities. For instance, in some businesses, a customer may be a function which maps the time to the status of the customer with respect to the service offering, in other businesses a customer may be more like a logical gate which decides to purchase or not.

Because they can be compact and highly conceptual, well-chosen mathematical abstractions can represent a large amount of information in very few entities and symbols, connecting the whole to the parts. That makes them particularly well suited to document large projects. They make possible, and to some extent easy and elegant to write, business objectives that need to be optimized.

While an equation can have very many terms, some of its aspects such as its functional form make it easy to grasp the idea behind it. By looking at the salient aspects of an equation one can get the gist of its motivation and see the whole picture, while looking at each term yields information on the details.

## Estimation

Quantities defined in the data can be estimated from the data. That estimation should be documented in the form of a method.

From calculating a simple average to solutions of more complex optimizations, good documentation should make clear how numbers are obtained.

It is not necessary to explicitly define the algorithm used. For instance, a quantity obtained as the solution of an optimization problem can be described by describing the function that is optimized and simply say that the quantity is the argument of the maximum of the function. How is this calculated, with which algorithm, may or not be specified, but if it is, it should be at a high level. For instance, it may be enough to indicate that a problem is a discrete optimization one and that simulated annealing is used to solve it. With that information, the code written will make sense, and one will find how the simulated annealing procedure has been implemented.

## Modeling

Statistical models relate observable variables or features to outcome that need to be predicted. At a high level they are almost all of the form y = f(x), a formulation that is so general that it says almost nothing other than a form of dependency. In this worst case scenario, the function f cannot really be made explicit. If it is fitted with some tree based method, then one may say that it is approximated by a function constant on rectangles and fitted by some tree based method. If it is fitted with particularly complex neural networks which architecture is data driven, then there may be not much else to say; but if the architecture obeys a logic, it should be documented.

Often though, much more can be said which express beliefs on how various quantities interact. These interactions can go from imposing some monotony with respect to some variables, some continuity, to much more specific ones, such as specifying a differential equations up to coefficients to be determined.

The section on modeling should indicate which algorithm is used to fit the model. However, that indication is not a full description of the algorithm. Indicated that least squares are used is enough, without specifying which specific version or implementation of least square is coded.

Custom designed algorithms need to be documented separately.

## Predicting

Often statistical models are used to make predictions. If the prediction steps are not a straightforward use of the model, for instance, if they are composed of several steps, then they may need to be documented. How is it done? What are the dependencies?

## Assumptions

Assumptions should be clearly specified. Some are mathematical, some are not and may reflect business assumptions. They are key to:

- improve model performance by relaxing or strengthening them;
- have an idea of the reliability, qualities and defects of the analysis on which a model is based
- sense how reliable a model is.

## Execution requirement or recommendation

It is often useful to document specific aspects of execution. While it should be obvious at this point if the model is estimated or run in real time or in batch mode, the latter raises the question on the frequency of execution.

Recommendations on when each process should be run should be made. How critical a schedule is should also be documented. Is it recommended to estimate the model every week? What can be tolerated if the process failed one week?

The recommendation that a model should be estimated as often as possible, while desirable from a statistical perspective, is not a valid one in terms of business. There are costs associated with computation, and some bottlenecks may limit the value of this recommendation: what is the point of updating a model daily if new data acquisition is done every Monday?

## Code pointers

Estimation procedures as well as model estimation are coded somewhere. While the entire project and some of the sub-processes may span hundreds of files, there are typically less than 10 files that implement the mathematical aspects of a single model used in a sub-subsystem. Hence, it is often possible to indicate which file to look at to see the implementation of what is described in the modeling document.

## Appendices

Appendices are sometimes needed to collect information that is needed to make the project reproducible, and contain information which otherwise will break the flow of ideas.

This information can be:

- data dictionaries;
- various information about data such as location or volume, whatever is useful to understand why some concepts have been put forward in the project description;
- frequency of data acquisition;
- specification of custom designed algorithms;
- performance in terms of statistical accuracy, risk, model confidence, prediction confidence, speed and cost of execution...

## Code documentation

Code documentation is probably the most familiar form of documentation. It sits in several levels, library, modules, functions and classes, specific lines.

Contrary to the modeling document which provides conceptual description for management, code documentation is intended for people who will read or use code. Therefore, it should be informative about the code, how entities and algorithms are implemented and may point to the modeling document for the more conceptual view.

The goal of code documentation is not to repeat the code but to help those who need to read it and those who need to use it.

Documentation higher in the hierarchy, at the library level, aims at giving a high level view of what the code accomplishes, possibly giving some caveats. This documentation should not repeat much of the modeling document but should work in concert with it, focusing on implementation, navigability, maintenance and usage of the code.

For instance, documentation in code may provide general information on how specific business entities and relations are implemented, tying the code to the modeling document.

Many code documenting systems exists. They often revolve around packaging comments placed in the code. While some give a better user experience than others, how the code documentation is rendered is less important than how thoughtful the code annotations are. But while not fully sufficient, a good interactive documentation tool is definitely useful.

## Final considerations

Many systems exist to build or publish online documentation.

They all share a common pitfall: by producing pretty output, they tend to shift the emphasize from meaning to aesthetics. Just like word-processors can make us think that a draft is final by beautifying our thoughts, pretty documentation is not good documentation: informative documentation is.

I have met many Data and Computer Scientists who find writing good documentation difficult, but like any skill it can be improved. Those who are good at it tend to like it, those who are not tend to dislike it.

The role of a manager when it comes to documentation is to point out the many facets and possible purposes of documenting to make the task at least interesting.

Personally, I like documenting because it gives me a chance to:

- step back and reflect on what I have done;
    communicate my vision, my opinion on a problem, with the hope of convincing others that it is not *the way* to go about it, but simply *a viable way*;
- get ideas on how what I have done can be applied to other problems;
- improve my deliverables as documenting forces me to put forward important concepts pertaining to the problem, which yields more reusable conceptual and code components.

Sometimes, because I want to be very thoughtful and need a lot of mathematics, I handwrite multiple versions, before typing them and polishing them further.

There are times where I help others document, or even document for others, which I find to be a good way for me to test if I truly understand what others have been doing.

It is very easy to incorrectly believe that one understands something, or to stop at a *high level*, which oftentimes is just half-understanding. Yes, this thing makes sense, or that thing makes sense… but when I have to write it down, do I know exactly what to write? Do I really know what we are talking about?

If I cannot write someone else’s thoughts in the form of a modeling document, *write the proper mathematical entities and models*, then I did not understand what was done and I need to go back and ask questions.

But having thought about it and having tried to write it allows me to ask more pointed questions, pinpoint what is it exactly that I did not understand, and rephrase the conversation in terms that are both my own and the others, bringing the team closer to the state of intellectual sympathy.

Because documenting forces me to step back, it often makes me realize that something I have done could be done better. It is therefore an iterative process, and I find that the process makes me better and teaches me valuable lessons. 