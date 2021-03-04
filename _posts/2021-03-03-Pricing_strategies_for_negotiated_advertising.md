---
layout: post
title: Pricing strategies for negotiated advertising
image: usd-2874026_1280.jpg
credit: 3D Animation Production Company from Pixabay
---

*Part 17 of 20 in a series examining the interplay of Data Science, AI, the media and advertising.*


## Buy-side pricing

How much should an advertiser pay to advertise on a given medium? 

The answer comes down to the ROI calculation outlined in part 7 of this series.  A simple enough concept in theory but not at all simple in its implementation.  ROI optimization is complex with a high degree of uncertainty in the data for several reasons:

1\. *What is the expected ROI of reaching one person in an audience segment?*

Some studies conclude that advertising is sometimes a waste of money with the target audience not paying attention to ads at all.  Others are adamant that the money spent is well invested. 

Since these studies are all on particular cases, others argue that “it depends” and that no one knows for sure! 
Resolving this debate is not the purpose of this article.  
An advertiser wanting to advertise has either:
- Some idea of the return frorn studies, an expert opinion, experience, or simply the Chief Marketing Officer’s crystal ball and authority! 
- The conviction that advertising is worth it and we have a budget so how do we optimize that budget.

Then one can determine the ROI for any given price, and, given a budget, one can elaborate a buying plan.

2\. *What is the waste?*

As we have seen in part 16, the view of “audience” from media’s perspective does not coincide with the view of audience an advertiser has, leading to wasted advertising dollars.  A good understanding of this waste is key to making a rational ad spending decisions. 
Several corporations sell data that give some estimate of the waste but the lack of integration precludes use of that information at scale.

3\. *What will each media option cost?*

Because buying advertising in traditional media is negotiated on a case-by-case basis it has very little transparency. 
There is so little automation of the workflows that advertisers do not have instantaneous access to prices. They must inquire of the different outlets about pricing then wait days for an answer from each!  This means they don’t have a global view of the market and how prices are evolving dynamically so they can make informed ROI optimization decisions. 

Armed with solid information on the above three variables advertisers could run massive optimizations and design advertising campaigns calculated to optimize ROI.  Unfortunately, none of the information on these three items is easy to access and manipulate in the current state of the industry.  (The Exchange proposal described in part 12 of this series would make substantial progress on the question of waste and could also help with the question of ROI per person in an audience.)  

Without this information, today most advertising decisions do not appear to be made very rationally.

The lack of consolidated information, connectivity to media operators, real-time realistic price estimates and systems to run scenarios means ROI cannot be optimized. 

The negotiated advertisement ecosystem will need to build these systems if it does not want to become irrelevant compared to the workflow of advertising in the digital world.

## Sell-side pricing

The sell-side pricing involves far more complex considerations. 

To start with, media outlets have no control on the demand from advertisers. They control neither how much money will be spent nor when it will be spent.

The seller owns an inventory, which is empty space in a printed newspaper or magazine, on a website, or on air time.  In the non-digital media, that space must be filled before the content is put in front of the audience. So, not only do the media operators need the money, they also need the content.

Unless a media operator is unavoidable because of their market position or high demand content (think Super Bowl on NBC), sellers of advertising space are in a position of weakness... 

In some aspects, sellers are very much like airlines or hotel, and could use similar revenue management techniques: forecast demand, estimate price elasticity of that demand, and maximize expected revenues. 

Applying the mathematical theory of revenue management they could segment their inventory into classes in terms of ability to obtain a refund prior to air time, priority codes, create artificial shortages, and raise some prices.

While this approach is sound, its applicability is currently limited because accounting for cost of opportunity is difficult with the current information systems.  

For example: Advertiser A requests its commercial be aired 3 times a week, between 6am and 8am on any 3 of the 5 weekdays. Such a request gives some flexibility to the broadcaster as to when the spots will be aired. Therefore, such an order should be less expensive per spot than that of Advertiser B who requests 3 spots at 7am sharp, one on each of the first 3 days of the week.  

But if Advertiser A also requests that no competitor shares the same commercial break, then, according to the industry, it may actually put more constraints on the broadcaster and generate substantial cost of opportunity.

The mathematics to handle this situation are known and sound. 

The problem lies two areas of data and the information that the current systems do not support:
1. demand forecast that takes into consideration the constraints that orders place on the inventory;
2. estimation of some price elasticities.

Let’s take a closer look at these two challenges to revenue optimization for media operators.

## Automated advertising contracting

Currently, advertising contracts are written in free text, very free text!  

No Natural Language Processing or AI system can interpret these contracts reliably enough to be useful in the industry. 

As a consequence, it is not possible to use past contracts to forecast demand according the constraints that they place on the inventory. This precludes using revenue management techniques and the considerable automation that would come with it.

These contracts contain some standard elements that have been properly isolated in some industry specific data exchange formats, such as advertiser name, address, amount of the transaction, start and end day of campaign, etc. 

But these formats fail to identify the constraints that advertisers may give to broadcasters other than by free text. That an advertiser does not want a competitor in the same commercial break remains a free text item in the contract.  The standard contract also fails to capture in a machine readable format what happens if the ad isn’t aired as planned.

Standards that have been implemented help make contracts machine readable but not machine interpretable. They have been designed to report on financial transactions, but not to automate contract execution. The workflow they have been designed for still requires a very large workforce.

The solution lies in understanding both, how media outlets price (in order to understand what part of the contracts must be made machine interpretable), and classifying the constraints. This is not a monumental task, but requires a combination of Data Science skills, business knowledge and vision possessed by very few in the industry.

The goal is not to have every single contract machine interpretable. Rather, the goal is to have the vast majority of contracts machine interpretable with no error whatsoever, and the few which are not machine interpretable clearly flagged for handling by humans.

To achieve this goal the industry needs systems that a) help users write these contracts, b) take over not only what is relevant to the financial aspects but also as much as the execution aspects, and c) let humans take care of the rare edge cases.

On the one hand the problem is a Data Science one as far as lack of needed information is concerned, and on the other a human-computer interaction as far as the system design is concerned.  

A complicated but solvable problem for which partial solutions have been already designed.

## Estimating price elasticity

In order to determine optimum prices through revenue management techniques, it is necessary to have an estimate of the price elasticity i.e. how the demand varies with the price. This estimate can be obtained by wishful thinking, conjecture or opinion irrespective of any data or, more wisely, based on solid data.

The current information systems give some partial visibility on the prices with some history of the negotiations for transactions that were made but not much, if anything, recorded about negotiations that failed. 

Systems must be built that track all pricing inquiries and negotiations, even those that do not end up in a transaction, as well as the causes of failure to close deals. This is a substantial human-computer interaction challenge, but again, one that may be tackled incrementally. As the complex systems are built, one can expect behavior to change, making that behavior more and more aligned with process automation.

Price elasticity is also dependent on the ability to substitute. Two factors that hinder calculating the impact of substitution on pricing are:
1. the lack of integrated information systems that prevent advertisers from generating scenarios that substitute market and media outlet, as we have seen in parts 5, 6, 7 and 10; and 
2. Media concentration.

The second point of media concentration plays at a couple of levels:
- *Market population*. 
In 2020, the top 25 out of 210 total media markets (12%) accounted for 50% of the broadcast television audience.  Advertisers running national campaigns have no choice but to buy most of these top markets which limits the market substitution options.
- *Outlet dominance*. 
Some media outlets have such a large reach and market share of audience that they are unavoidable to buy.  In Atlanta, ABC’s “World News Tonight” on WSB-TV had a 13.4 rating and a 25 share in April 2020, meaning that 13.4% of the households with televisions tuned in, and 25% of the households watching television at that time watched that show.  The station claims to reach 95% of the Atlanta market overall.

Given the complexity of advertising contracts including substitution, the next challenge in building price elasticity models is the vast amount of data that it requires. Individual media outlets don’t have the necessary information so a solution requires pooling information as the Exchange concept proposes.

## Other seller pricing strategies

The problem with pricing strategies derived from revenue management principles is that they implicitly assume a large pool of customers, so that statistical, or averaging, arguments can be used.

Between the Super Bowl advertiser and the everyday standard advertising contract of most ad buyers, lie important customers of media operators who aren’t standard or extreme but still unique in some way.  

They may book an entire yearlong campaign or they may be repeat buying year after year.  This reliable revenue stream makes them nearly indispensable to a media operator and not subject to the classical calculus of demand responding to prices via elasticity. They require a different strategy, which necessitates more collaboration between the buyer and seller.

To automate this critical pricing strategy scenario it is important to keep in mind that the goal is not to have fully automated systems making decisions, but to build decision supporting systems which help humans make faster and better informed decisions.

Thus, a simple model that would go a long way to speeding up the process would: 
- track the past record of an advertiser with a media outlet or a media group,
- present the information in a meaningful way,
- suggest a price based on past prices and budget goals to achieve,
- with some explanation as to how this price came about
And of course , would do all this with an adequate user experience which requires no tech expertise.

## Conclusion

Pricing, particularly on the sell side, is probably one of the most complex issues to tackle in the automation of the media/advertising workflow as traditional edited media fights for survival.  

It requires a vast amount of information, some touching contracts and constraints that these contracts place on media outlets. 

It requires a large number of sophisticated models to be built, as well as workflows based on different models and yet provide a seamless user experience. 

In the current state of the industry, it must also yield control of the flow of money to the people involved in the negotiations and transactions. 

And, models must remain within the legal framework that limits price data sharing and prevents collusion.

These challenges are substantial, for sure. But one should also keep in mind that no one expects to transform the industry over night. 

Four stages of pricing automation development and maturity are obvious:
1. prices that allow for running large numbers of scenarios to plan a campaign;
2. prices that are recommended to the sell-side as the basis to meet budget goals;
3. prices that can be the basis for starting a negotiation toward a transaction;
4. prices that can feed into automated transaction systems, with human supervision and interaction.

The current stage is stage 0.

So far, companies in the industry have failed to recognize a viable path toward automation, have tried to tackle ill-defined problems, and have added layers of complexity. This is why the industry is in its current state, losing profitability and losing control of its revenues to digital workflows.

Solving the problem of pricing is complex with many challenges. Ten years ago, Google tried and gave up because auction pricing did not fulfill the needs of the industry, but that’s what makes the industry so interesting to Data Scientists.

To me, this challenge is an opportunity to build amazing teams doing amazing science and business for the noble cause of the free press.
