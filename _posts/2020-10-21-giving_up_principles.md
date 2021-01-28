---
layout: post
title: Giving up principles
image: archimedes-principle.jpg
credit: www.oldbookillustrations.com
---
It is said that Data Science is a combination of statistics, computing, and business... three disciplines with underlying core principles. 

Some of those principles are very basic.  A basic principle of doing business is to find a problem that people encounter, find a solution, and sell it to those who need it. 

Some are not so basic.  The technical nature of statistics makes its principles harder to communicate and understand requiring lengthy and specialized training during which critical principles are ingrained.

While principles within the individual domains of knowledge are consistent, as a Data Scientist in the Corporate world I’ve encountered situations where the needs of the business collided with my beloved statistics principles forcing me to abandon them.

The French philosopher Gaston Bachelard described mental blocks (“epistemological barriers” in his words) that hold scientific minds back from making progress, beliefs that we cling to while the circumstances require us to dispose of them.  Good researchers are able to get over these epistemological barriers but it requires imagination, the ability to look at problems with a different mindset, a different lens, and the courage to go against our own beliefs.

Since my move from academia to the business world I’ve had more than one opportunity to apply Bachelard’s lessons.

The first came when I asked to speed up a computation for selecting models.  Among all these models some were special cases of others. 

If you are not a data scientist, picture a piece of paper with a line drawn on it with a point on that line. The statistical principle of **parsimony** asserts that one should aim for models with the least number of parameters. If a point is enough to express what I want then I shouldn’t draw the line.  Parsimony is a principle of laziness… build models as small as possible… which makes sense because smaller models need less observations to be estimated, or, put differently, with a given amount of observation, the estimations of a smaller model tend to be more accurate than those of a sprawling one.

In the business case I was dealing with the principle of parsimony was giving incentive to have many models to choose from then selecting the smallest one to fit the data.  

However, if the business was willing to lose a bit of accuracy (about 10%) and not seek the smallest possible model but one that was “good enough” we could double the speed of the computation, which was critical for the company.  We gave up on the parsimony principle.  

In this case the epistemological barrier was not particularly high because the constraints were such that it seemed the only way forward. The problem and the constraints lead us to a fairly natural solution.

Overcoming that barrier was not as easy for me in a more complex use case involving the core statistical principle of **minimizing bias and variance**.

In this situation the models were generally performing fine. There was an industry standard with the consensus that predicting with an error within 25% was good.  

But in some cases, the predictions were far less accurate, 50%, sometimes even 100% error, were possible. Everyone in the industry was struggling with the same accuracy problem with the general consensus that fairly bad data quality precluded better predictions.  

In other, critical instances it was known that the algorithms were poor, and “experts” were relied upon to make predictions. These experts were using fairly basic information but in a way that was particularly hard to reproduce in a model, the type of situation where one would need to look at all sorts of cases … in this case to this, in that case do that, in this other one, do that, and so on. 

For Data Scientists the most frustrating situation is a seemingly endless number of cases.  In this case, paradoxically, the trickier the rule became, the more critical the prediction was because the more money that was at stake! 

Yes, the algorithms could replace humans when it was obvious and the human task was simple, painless, fast, and not so consequential, but were failing when the human task was complex, expensive to do, and really important for the business.

But it wasn’t just the “machines” that were failing, it was the machines and the people programming them!  

Every technology is designed to do some tasks well, can sometimes be repurposed by skilled operators to do other tasks well, but often fails at doing tasks it is not designed to do.

Why were the predictions failing so badly?

The process to fit a model is quite simple: get some data, pick a model, and calculate the parameters of
the model so that it fits the data the best. Eventually, through trial and error with different models, pick the best.  

There is a caveat though.

On the one hand, if the size of the model (measured by the number of parameters) is comparable to that of the data, then the fit will be very good as the model has a lot of parameters to adjust itself to the data.  But, if too specific to the data; such a model will not predict well. 

On the other hand, if the size of the model is too small it won’t capture well the complexity of the phenomenon being modelled.

The statistical principle of **minimizing bias and variance** advises having enough parameters to fit the data well (minimizing the bias), but not too many so that the resulting estimates are reliable (minimizing variance).  

Basically, a model should fit, not under-fit or over-fit. 

Under fitting is not much of a danger because there are excellent tools to detect it.  In contrast, over-fitting is more subtle and while tools exist to detect it, they are more sophisticated and require more expertise to be used wisely.

Data Science curriculum constantly warns students that over-fitting a model is dangerous and they should be very careful about the number of parameters if they want to build models that make good predictions.  Avoiding over fitting is Data Science dogma and over the past 40 years many methods have been designed to limit it.  I know, I’ve taught it many times.  

One day, I finally passed that difficult epistemological barrier on this project. 

Hidden in the all the cases that the experts were delicately coming up with, the reason models were so bad is that they were fitting but not overfitting.  

Translated into Data Science terms (and it was not an obvious translation at all) the experts were grossly
overfitting!  A truly unique situation where the principle of not over-fitting didn’t apply.

A few hours of coding to increase model size beyond “reason” as ordained by the principle and suddenly the average prediction error went from 25% to 16%, which was once unthinkable and now
beating all the experts!

The principle failed, and we failed with it until we saw it for what it is: a dogma which needed to be questioned.

Yes, principles are important… as guides… as guardrails along a winding road.  Critical if you are traveling by car as you most often are on a winding road. but there are times when you may need to leave your car to clamber over the guardrail to get to the prize on the other side. 

Bachelard’s epistemological barriers are reflections of our perception of our environment and how we navigate that environment. To get over them means to look at problems differently, to realize against all beliefs that in the specific circumstance we are in, the car may not the best way to travel, and that going by foot is more efficient.

Should we give up all principles? Certainly not!  But every principle should probably be left on the side of the road at least once.