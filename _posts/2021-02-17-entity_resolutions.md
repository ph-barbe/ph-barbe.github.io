---
layout: post
title: Entity resolutions
image: banner-1090830_1920.jpg
credit: Gerd Altmann from Pixabay
---

*Part 15 of 20 in a series examining the interplay of Data Science, AI, the media and advertising.*

You say tomehto, I say tomahto.  

When a legacy industry has many players, each with their own legacy systems and business processes, the terms used to describe the same thing often vary across the industry. 

This is the ***entity resolution problem***: what are the different names for the same object and how can we identify that object when different people name it differently?  The problem occurs in many parts of the media ecosystem.

In this article we will look at examples of this challenge, in increasing complexity, and discuss their solutions at a high level.

## Very few objects

The simplest entity resolution problems can be solved by using rules that are coded to be understandable by machines. This is typically the case for the following:

- audience segments: W2554 vs. Women 25 to 54;
- time of the day: 2pm vs. 2p vs. 1400
- different calendars: Monday 2 am on regular calendar which becomes Tu. 2am on a broadcast one;
- different day names: July 4th vs. Independence Day.

The identity resolution problems these examples create tend to be easy to solve, because the number of variations of names and entities are very limited.  Hence some matches can be coded, and systems can be enlarged to adapt to new rare cases.

Slightly more complicated are entities that depend on specific media outlets and even specific contexts. For instance, a broadcast day starts at different times on different television stations, and some exceptional broadcast days may be longer or shorter than 24 hours. 

But again, those typically obey some rules that are not particularly complicated and can be coded. The complexity is twofold:
- these rules may not be inferred from data and may require some business knowledge;
- they require complex changes if they have not been considered in the analysis.

This is the case for the start of the day in the broadcasting industry which depends on the television or radio station.  If systems designers assume that a day has 24 hours and can get by with the regular calendar, then accommodating longer days may require major changes in how the system is coded, resulting in high development costs.

In these simple cases, the key to maintain accurate information is a collaboration between machines and people, automation being done as much as possible at the system level, and users in each media outlet either validating or updating information.

## Media outlet names

More complicated is the problem of identifying media outlets.  

Is it the NYT, New York Times or The New York Times?  In the broadcast industry, WSB-Atlanta and WSB-TV refer to the same television station in Atlanta. 

The problem is more complicated when one considers broadcast translations which typically carry much of the same signal as the original station but may offer a different signal for advertising, making it for advertising purposes, a separate station. 

There is WSB-TV channel 2, but also WSB-TV channel 31, channel 46, channel 17 and channel 14.  Some systems make a distinction, others don’t.  At the current time, these WSB stations are all the same as far as content acquisition is concerned, but could be different in the future, and could also have different programming. 

Sometimes the context can help solve the entity resolution problem. What is referred to by WSB? There is a TV station WSB-TV, and a radio station WSB-FM.  According to the context it is one or the other. 

Add then the complexity of affiliation. One may speak of buying “ ABC locally in Atlanta” which refers to WSB, the ABC affiliate in Atlanta.

It does help that there are lists of media outlets, owners, affiliates, etc. and so the possible entities are known.  Natural language processing techniques allow identification of most of the entities, and people can settle the unusual cases.

But names change over time: call signs, owners, affiliations, everything changes.  Thus systems must be aware of changes when they occur and react promptly.  The matter is particularly complicated for entities that change identifiers: this change is meaningful in some use cases, not in others, and some systems may stick to older names.

Tracking the graph of relations between these entities and the changes, and building systems that navigate these graphs effectively both in the relations they express and in their changes over time, while not tremendously complicated, is not simple.

The bigger point is not that these problems must be solved to provide more automation because solutions are well known.  The challenge is that these entity resolution problems add considerable complexity to automation because of the knowledge of the business needed to build the proper solutions.

## Identifying content

Some content has been identified with different names in the media industry. 

For instance OpEd page and opinion page are usually the same. This situation is easy and a list can be built of names under which that page is known.

As we have seen in Part 13 and 15, there are many types of audience measurements available, which are the basis for forecasting. The drawback of having many vendors and many measurements is that, inevitably, each come up with its own way of referring to entities such as the title of a program. A system may have a limit in the number of characters that forces abbreviations, and users of one system may enter GD M AM, while in another system, this may appear as Good Morning America. How can we make the identification that these names refer to the same entity?

In some instances, identification of exactly what is referred to can be made on time especially for programs run on schedules.  Yet it is still easy to find discrepancies between the scheduled programming and what content was actually aired.

Then there is the use case of buying air time in the future where the programming is uncertain, and no specific air time is specified.  For instance a commercial order may refer to GD M AM M-F, meaning Good Morning America, Monday to Friday, and that entity needs to be identified.

And new content is constantly created generating a variety of names referring to that content. 

In the newspaper industry, content identified by article name brings new entities at an astonishing rate. 

In the broadcasting industry, about a third of the titles are new each year. A new title appears first in a system tracking what will be aired. Then when it is aired, it may have a different title. 

Hence the question of identity resolution is also dynamic and is at time the broader problem of identity management.

The complexity stems in part from the number of entities that need to be tracked. To give you an idea, 1,600 commercial television stations in the US represent roughly 14 million distinct programs each year.  But program names are far less, of the order between 50,000 and 100,000 names depending on how they are written, made in a vocabulary of anywhere between few thousand to more than 50,000 words. That leads to a combinatorial explosion for matching different names that precludes using any naive methods relying on pairwise comparisons.

Then we have the matter of genre.  In part 14, I described why it may be needed to base audience forecast not only on exact content but also on genre.  The genre of content is usually assigned by humans. Beyond the usual clerical mistakes that are to be expected, employees come and go, judgement may change, resulting in data inconsistency. In some outlets such as newspapers, content may be given a too granular name, like the title of a piece, or a too generic genres where nearly everything is categorized as either news or opinion, resulting in an ineffective taxonomy.

Some mathematical techniques using morphisms of partial orders, combined with natural language processing tools and ad hoc string distances have been particularly effective in some of these problems, but they are not widely known.

Ultimately, the entity resolution problem for program names is difficult but manageable because it is easy to have a reasonably clean master list of television and radio schedules. A combination of machine learning / AI techniques and the help of experts to settle odd cases achieves excellent results.

## Identifying advertisers

Of much greater complexity is the entity resolution problem related to the various names referring to the same advertiser.

To appreciate the significance of an advertiser as an overall customer, media outlets want to know…  How much has this customer spent so far?  What is the prospect of this customer spending more?

The problem is that a company executing an advertising campaign may go through different ad agencies and appear with different names in the different systems of a media company. 

Some advertisers have different levels of advertising … national, regional, local.  Different parts of their corporate structure may be involved and in some cases it is useful to identify them as part of the bigger corporation, while in others it is not.  Some corporations have whole subsidiaries that appear as totally distinct entities on advertising contracts.

Identifying the relationships between all these entities of the same customer requires deep business knowledge on the part of a media company to see the total current and future value of that customer.

## Challenge of the transactional environment

These many cases of entity resolution problems are not simple to address but can be solved, and to some extent have been, except the problem of identifying advertisers. 

While one could solve these entity resolution use cases independently, the industry needs to use those solutions in further systems. This means that more machine learning and AI needs to be built on top of these solutions to make them actually useful to the industry.   Of course, this adds more layers of complexity when considering the systems that are required.

The biggest challenge is inherent to the transactional aspect of what needs to be automated. Ultimately, the media and advertising industries need automation to bring efficiency in how decisions made and transactions executed.  

With millions of dollars at stake these systems must be particularly reliable.  A commercial seen by the wrong audience, aired on the wrong show, printed on the wrong magazine are catastrophic errors costly for everyone… advertiser wasted money, outlet wasted inventory, the intermediaries failed. 

This is why the industry needs decision supporting systems not decision making systems.

There have been many spectacular use cases of AI in the recent years.  For example, image recognition can be made amazingly accurate for checking IDs at borders and the 95% accuracy of  language translation software is amazingly useful to a tourist (not so much to negotiators negotiating the fine details of an international treaty).

The transactional nature of the media and advertising industry we seek to automate combined with the vast amount of money involved, demands that systems built to support decisions in the media industry must have flawless performance.  Not just of the system alone, but of the system used in context, with human interactions. 

These systems are challenging to build but the progress so far indicates that solutions can be built to move the industry forward.
