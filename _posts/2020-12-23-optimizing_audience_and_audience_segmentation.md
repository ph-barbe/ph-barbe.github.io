---
layout: post
title: Optimizing audience and audience segmentation
image: daria-lisovtsova-oNXK1F8cVaE-unsplash.jpg
credit: Daria Lisovtsova on Unsplash
---

*Part 7 of 20 in a series examining the interplay of Data Science, AI, the media and advertising*.

In previous articles we’ve examined the stunning fragmentation of the media landscape, in terms of both the rise of new mediums and the explosion of outlets with each medium. 

While technological progress has made running a media outlet more affordable, surviving and thriving has always depended on garnering an audience… the touchstone of all media.  

## Speaking to an audience

From the beginning, advertising has been based in some degree of audience segmentation. A billboard aims at those who will be in that location.  A radio program is aimed to those who will listen at that time.

People have different interests, hobbies, passions, that they want to both share and enrich in interacting with similar people to reach and they sometimes need goods or services to satisfy their interests. With limited resources, reaching the audience that is most receptive to what they have to offer is crucial for advertisers (and thus media) making audience segmentation essential to success for both parties. 

Over time, audiences have been sliced and diced into ever finer pieces based on innumerable characteristics that range from simple geographic location to what is termed psycho-demographics. 

A perennial problem for advertisers with their limited resources is attained the optimum balance between breadth and waste.  As an example, take a golf club manufacturer who wants to reach golfers or golfers to be. Money spent to reach a broad audience that includes most everyone will snare some people interested in golf clubs but it will be wasted on all those with no interest in golf.  Money spent to speak only to golfers or golfers to be would be a much better investment even though the cost of reaching this more specific audience may be higher per person.

For the media industry, the desire to segment the audience for advertisers, combined with the technological and financial ability to create more media outlets has made it a viable business model for outlets to cater to a few hundred people and monetize that audience to advertisers. Up to a point, as we will see in the next article.

For advertisers, the desire to limit waste that drives them to seek segment audiences leads them to want to acquire more information about the audience.  The big tech companies’ success in advertising stems from their ability to precisely segment the audience into very specific niches.  By analyzing user-generated content in complex ways they (theoretical    • volume: you may get a discount from a media outlet if you advertise a lot, you may give a volume discount to buyers that reduces your profit on that sale.  
    • location: advertising cost for outlets in New York vs. outlets in other areas area, buyers of swimsuits in Florida will presumably pay more than in Minnesota. 
    • time of the year: demand from big box retailers around Black Friday takes up all the media inventory driving advertising prices higher.  People will pay more for a winter coat in January than in July.

![image](/assets/images/roi_advertisement_investment.jpg){: style="max-width: 40%; height: auto; float: right; padding: 3%"} 
If it costs $1 to reach a person,10% of the people we reach buy, and we make $50 profit on each sale, then reaching 200 people costs $200 and generates 20 sales at $50 per sale.  We bring in $1000 profit at a cost of $200 leaving us a net profit of $800.  A simple example to be sure but much more complicated in reality.

For starters, we can’t reach every prospect using a single medium. But we can sort the mediums by cost per prospect, start with the cheapest and go up from there.

To keep things simple, if the ROI per prospect remains constant, this is represented by the following graphic, where:

- the horizontal axis measures the number of prospects reached,
- the blue line is the anticipated revenue, proportional to the number of prospects reached,
- the red line is the cost of advertising, which is not only increasing in the number of prospects, but also increasing as the medium changes (hence the different red segments, with increasing slopes).

Profit, the gap between the blue revenue line and the red cost line is maxed at the green vertical line which tells us how the optimal number of prospects we should reach.

This basic model does not need a Data Scientist to be implemented!

## Traditional segmentation

As technology was enabling fragmentation of the more traditional media it also fulfilled the desire of advertisers to segment the audience into fairly coarse, basic categories… geography, gender and age.  

With just these 3 segmentation criteria how complex is the calculation for advertisers putting together a campaign to reach their targeted prospect, sales and profit numbers? 

In the U.S.     • volume: you may get a discount from a media outlet if you advertise a lot, you may give a volume discount to buyers that reduces your profit on that sale.  
    • location: advertising cost for outlets in New York vs. outlets in other areas area, buyers of swimsuits in Florida will presumably pay more than in Minnesota. 
    • time of the year: demand from big box retailers around Black Friday takes up all the media inventory driving advertising prices higher.  People will pay more for a winter coat in January than in July.

Age has typically around 8 brackets, which can technically be combined 28 ways but some combinations are useless, 10 is common. 

With just these basics we have 210 x 2 x 10 = 4,500 possibilities. Add a bit more information an advertiser can acquire about audiences and the number of possibilities can climb to 100,000!

Multiply this by the number of media outlets… and now you are talking about the need for specialized knowledge to even think about a problem of that size.

## Complex optimization

In the real world, the ROI model described in the graphic is too simple to be useful as both the cost and revenue lines are each impacted by all sorts of    • volume: you may get a discount from a media outlet if you advertise a lot, you may give a volume discount to buyers that reduces your profit on that sale.  
    • location: advertising cost for outlets in New York vs. outlets in other areas area, buyers of swimsuits in Florida will presumably pay more than in Minnesota. 
    • time of the year: demand from big box retailers around Black Friday takes up all the media inventory driving advertising prices higher.  People will pay more for a winter coat in January than in July.
.  
- location: advertising cost for outlets in New York vs. outlets in other areas area, buyers of swimsuits in Florida will presumably pay more than in Minnesota. 
- time of the year: demand from big box retailers around Black Friday takes up all the media inventory driving advertising prices higher.  People will pay more for a winter coat in January than in July.

If you are going to run a campaign on multiple outlets, your costs will depend on the outlets you choose and as we have seen, there is more than a large choice… more options than a human can grasp!  Now factor in the uncertainty that comes with the choices you make… how do you know how many people will actually watch the TV show you just bought a spot on?   

Once all the variables are incorporated along with all their uncertainty, the optimization of your advertising spend becomes extremely complicated.  Addressing this challenge requires a combination of classical optimization methods that are reasonably well understood, with more complex and less known techniques of combinatorial optimization. 

The volume of information may be large, as well as the number of variables which incorporate all the flexibility that one has in planning a campaign. This yields very large optimization problems which are very difficult to solve, even with the most powerful cloud technology.

Specialized knowledge and vast amounts of information are required just to setup the problem properly, and more knowledge to actually solve it.  

More information, when well used to optimize results, yields a better ROI… sounds like a challenge (opportunity)  ripe for solving by Data Science, AI and computers!  Why does the industry lack the technology and automation to do this work?

The answer lies not only in the need to build teams of Software Engineers, Data Engineers and Data Scientists that don’t necessarily need to be big teams, as computers can handle the volume, but they do need to be highly skilled.  And they need to have the correct vision. That vision requires a mix of technical and business knowledge that few have, which is why the industry lacks automation.
