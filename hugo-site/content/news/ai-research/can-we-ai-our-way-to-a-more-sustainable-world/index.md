---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-20T18:15:43.334651+00:00'
exported_at: '2026-04-20T18:15:46.012714+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/podcast/can-we-ai-our-way-to-a-more-sustainable-world
structured_data:
  about: []
  author: ''
  description: Doug Burger, sustainability expert Amy Luers, and optimization researcher
    Ishai Menache examine the global emissions implications of datacenter operations,
    efficiency gains, and AI's potential across electrification, materials, and food
    systems.
  headline: Can we AI our way to a more sustainable world?
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/podcast/can-we-ai-our-way-to-a-more-sustainable-world
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Can we AI our way to a more sustainable world?
updated_at: '2026-04-20T18:15:43.334651+00:00'
url_hash: 4fd67968903e88cdc1148281022c09debfe563c8
---

So maybe I’ll first turn it over to Amy. Can you tell us a little bit about your job at Microsoft and what got you into this space, maybe a little bit of your story?

**AMY LUERS:**
So as you said, I lead the sustainability science and innovation in the Microsoft Corp sustainability team, which really means I get to work with really smart people around the company, around the world, at MSR [Microsoft Research], on shaping and informing sustainability solutions for Microsoft but also for the world.

And part of that is leading our strategy on AI and sustainability. And how I got into it, I’ve been working on sustainability and climate my whole life. And I’ve worked, from the tech sector, I was at Google actually previously. Also was in the White House working at the intersection of the CTO’s office and environment and resources and energy.

I also led an international research institution, UN-based network rather, focused on sustainability. And in that context, after coming out of Google, where I was really … started to think about the power of compute and digital tools for transformation, and— which is why I was brought into the White House to work at that intersection—when I started leading the sustainability network, research network globally,
[Future Earth
(opens in new tab)](https://futureearth.org/networks/)
, I really brought this need to think about innovation and digital technologies in that space.

And I will say the sustainability science network at that time, you know, it was 10 years ago, eight years ago maybe, was a little resistant to thinking about AI and technologies in this space.

And I started a global initiative called Sustainability in the Digital Age, where I really brought together the digital technology and AI community. It was in Montreal, which there’s a lot, a big AI community there,
*and*
the sustainability scientists globally. And really started to think about what are the potentials, what are the risks, and led a big international study to put together a research and innovation agenda in this space.

And that sort of really shifted my approach from just “big compute can help things,” which I was really focused on at Google, to this role of AI and machine learning in this space.

**BURGER:**
And, Ishai, so you are a world-renowned expert in, now, ML and optimization. You know, you’ve published extensively. You’re, I think, famous in your research community. You’ve had, I think, broader—you’ve had a lot of impact on Microsoft’s business. You’ve also been
[published in the Harvard Business Review
(opens in new tab)](https://hbr.org/2025/01/how-generative-ai-improves-supply-chain-management)
.

So, you know, you’re a little bit polymathy and sometimes a little intimidating to me.

**ISHAI MENACHE:**
Yeah. [LAUGHTER]

**BURGER:**
You know, but I’d like to hear a little bit about your background, just, you know, a short version of your story for the listening audience.

**MENACHE:**
Yeah. My background is actually in engineering. However, my graduate studies were, as you mentioned, like in ML, reinforcement learning, and later on distributed optimization, game theory, a little bit more on the theory side.

So my story is that when I was doing my postdoc at MIT [Massachusetts Institute of Technology], you know, the cloud was kind of on the rise, circa 2009 or so. And I got fascinated by the cloud. My initial interest was actually in the economics of the cloud and, you know, pricing. How you price the cloud. And I got to know about MSR because, you know, around that time there was a new kind of lab opening just by MIT, MSR New England. And I got fascinated by the cloud and, you know, not only the economic aspects of it, but more fundamentally, you know, how do you utilize resources more efficiently?

And that’s what got me to Microsoft Research in 2011. So I was consulting in MSR New England but then moved to Redmond in 2011 to join a lab called Extreme Computing group that was actually dealing with the cloud futures.

And if I can mention, Doug, you were also part of that, so …

**BURGER:**
That’s right.

**MENACHE:**
I’ve known you for quite some time.

**BURGER:**
Yep.

**MENACHE:**
And, you know, so sort of my, let’s say, my angle into that, so there were like a lot of systems people thinking about the, you know, infrastructure of cloud. And then at the other extreme, there were theoreticians. They were thinking about like, you know, the next kind of wave or like, you know, innovating in the area of algorithms.

But I think what was sort of missing is a little bit of bridging between, you know, algorithms and then cloud infrastructure. And that’s where I sort of found a very interesting niche for myself, and later on, for the group, which I founded in 2019.

**BURGER:**
So you recently announced the system called
[OptiMind](https://www.microsoft.com/en-us/research/blog/optimind-a-small-language-model-with-optimization-expertise/)
. And I, you know, I did a
[LinkedIn post
(opens in new tab)](https://www.linkedin.com/posts/dcburger_model-overview-activity-7417935419067113472-1954/)
about it because I was really excited about it.

And just tell us what the system does, like why … it got a lot of attention. So what does the system do? And then maybe we’ll dig a little bit into optimization for the audience. And then, but then we have to get back to AI.

**MENACHE:**
For sure. So, you know, stepping back a little bit. So what is actually
*optimization*
or
*mathematical optimization*
? So optimization or mathematical optimization is a way of using mathematics to make the best decisions when there are many choices and some limitations. OK.

And, you know, just a little bit more, you know, concretely, so in every optimization problem you have, first of all, a description of the problem that you need to solve. Then you have a bunch of decisions that are actually, in mathematical terms, these are the variables. You have an objective. What is your goal? What are you trying to optimize?

It could be something that you’re maximizing, revenue, but it could be that you’re minimizing costs, so there are different versions or different kinds of goals or objectives. And then there are constraints, which is like you cannot do whatever you want. There are some sort of limitations such as capacity constraints in the cloud setting or other factors that you have to account for in order to come up with the best possible decisions.

**BURGER:**
So what … so maybe a simple … just to be silly for a sec, so I have a, you know, complex drive to work, and one day I find that the way I usually take is blocked and my brakes are really worn and I can only stop twice. So your framework might be able to figure out, like, what path gets me there saving the most gas.

**MENACHE:**
Right. So that’s one example. And maybe you don’t want to pay for tolls for some reason, so that limits, you know, the roads that you can take. You know, there’s speed limits and such things. These are all constraints that you have to account for.

**BURGER:**
There might be some speed traps, but I’m willing to go by a speed trap if the route is much shorter.

**MENACHE:**
Maybe.

**BURGER:**
So stuff like that. So it gets pretty complicated, doesn’t it?

**MENACHE:**
Right. It gets pretty complicated because especially when the, you know, maybe you’re a single driver, but in optimization settings, think of like some of the problems that we worked on actually with the
[Dynamics 365](https://www.microsoft.com/en-us/dynamics-365/what-is-dynamics-365)
was also in the context of field service, which is about managing technicians at scale. So think of like not just you, but thousands of technicians that have to fulfill or that have to take care of certain work orders. So it would be thousands or tens of thousands of work orders.

And then you need to assign the technicians to these work orders. And there’s a bunch of constraints. Maybe not every technician can do every work order. You have to account for the traveling of the technicians, right. So it’s like you’re not going to send a technician that is in Spokane to do something in, let’s say, in Seattle because, you know, all day will be wasted on traveling.

**BURGER:**
And it’s not sustainable.

**MENACHE:**
It’s not sustainable. [LAUGHTER] And also, you know, the gas, obviously. So all these kinds of considerations, you can map it formally into mathematical optimization. And then there are techniques of solving this problem to optimality.

So essentially there is some machinery and there are experts that can take these problems and come up with the algorithms, but not everyone can do it. So it requires some expertise. In fact, graduate-level expertise in operation research or in, you know, algorithms, computer science type of algorithms. And when gen AI was emerging, we saw an opportunity to democratize optimization with gen AI in the following sense that a person that is not an expert can define what they want to do.

You gave your example about, you know, getting to work. It could be like, you know, a simple example of packing, which is like I have a suitcase that I, you know, I have a limit of, like, 20 pounds. And I have a bunch of things that I have to … that I want to fit in like, you know, I have with certain importance. Some are more critical, like, you know, I don’t know, like my laptop, and all that. But then there are books that are quite heavy, and maybe I still want to read books.

**BURGER:**
Or I’m running an airline, and I have to schedule the flights, and I want to minimize fuel.

**MENACHE:**
Yeah, that, too. And essentially, so you want to be able to describe what you need to solve in plain English, specify the problem, say what the decisions are, like I mentioned, like what your goal is, and then what constraints need to be accounted for.

And you want to use AI that will help you take all these considerations and essentially formulate the algorithm itself. So write down the recipe, the mathematical recipe, that would produce an optimal solution.

**BURGER:**
Got it.

**MENACHE:**
So that’s what OptiMind is about. [It] is a small language model that was trained especially for this kind of scenarios of, you know, taking natural language and mapping it into an optimization algorithm.

**BURGER:**
So this is really great, and I think we’re going to come back to this. I want to now go back to Amy. When we think about AI and these datacenters that the industry is building and they, you know, they use water, they use electricity, you know, there’s contention in some communities about them being placed there. If I, you know, I’d love to be really data-driven and just kind of very factual.

So if I look at the overall picture, like, what is the real impact we think of this transition on, you know, climate, sustainability. And it’s complicated, right, because there are many sources of emissions? Electricity gen is one, but you have renewable energy. But it takes materials to build these things. So can you kind of give us some framing to help us understand it?

**LUERS:**
Yeah. So first of all, you know, I think when we think about AI and climate, a lot of people think about just the infrastructure side. And I think it’s really important to think about this holistically. I actually personally believe that AI will be one of the most influential factors determining our climate future, for better or worse. But I also believe that we actually need AI to solve the climate crisis. So with that as context, let’s talk about the infrastructure, remembering we have to really think about the full context. You know, let me put this into context.

So from a climate perspective, what matters is the emissions to the world, the emissions of greenhouse gases to the world, heat-trapping gases, …

**BURGER:**
Right.

**LUERS:**
… to the climate, not specifically energy, right, because energy can be in different forms.

**BURGER:**
Right. It’s, what are you putting in the air?

**LUERS:**
What are you putting in the atmosphere?

**BURGER:**
That’s right.

**LUERS:**
So, you know, if you think about it from a global perspective, the world uses about … energy itself accounts for about
[75% of all of the emissions that go into the atmosphere
(opens in new tab)](https://www.wri.org/insights/4-charts-explain-greenhouse-gas-emissions-countries-and-sectors)
.

**BURGER:**
Wow, that’s a lot.

**LUERS:**
So that’s a lot. But a lot of people think it’s the whole thing. So there’s other things that are not energy. [LAUGHS]

**BURGER:**
OK, three-quarters, three-quarters …

**LUERS:**
But in the context of … so from a climate perspective,
[datacenters account for about .5, less than .5% of all emissions as of 2024
(opens in new tab)](https://www.iea.org/reports/energy-and-ai/)
.

**BURGER:**
OK. But they’re growing?

**LUERS:**
But they’re growing. And so if you’re growing and you think about … there are lots of projections. It’s hard to project really beyond a couple years, as you both know, because things are changing so quickly, both on the demand, on the efficiency, what we’re using. Are we going to be using small language models? Like, we don’t know what the future looks like.

The IEA [International Energy Agency] projects
[by 2035 that the, the electricity use could double
(opens in new tab)](https://www.iea.org/reports/energy-and-ai/)
. And so from electricity use, actually, datacenters use about
[1.5% of global electricity
(opens in new tab)](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
,…

**BURGER:**
Yup.

**LUERS:**
… and that could double, could be between three and fi—
*even more than double.*

But that’s still, from their projections, it would still be less than 1% of
*global*
emissions. So even if that would double in that space. So it’s still in terms of a global emissions perspective, which is what the climate cares about, …

**BURGER:**
Right.

**LUERS:**
…it’s a small percentage.

**BURGER:**
Can I just go back for a second, break that down?

**LUERS:**
Yeah.

**BURGER:**
So, so energy is
[three-quarters
(opens in new tab)](https://www.wri.org/insights/4-charts-explain-greenhouse-gas-emissions-countries-and-sectors)
, of … generates three-quarters of emissions. But that includes burning fuel, …

**LUERS:**
Yeah.

**BURGER:**
…transport. And then what fraction of that three-quarters or let’s say just total emissions do we think electricity is?

**LUERS:**
So electricity …

**BURGER:**
Generation …

**LUERS:**
…is about 20% … or, no, electricity … the energy that’s produced is consumed … about
[20% of it is consumed as electricity
(opens in new tab)](https://www.iea.org/reports/electricity-2024/executive-summary)
.

**BURGER:**
Got it.

**LUERS:**
Now, in terms of emissions, about
[35% of the emissions from energy is from electricity
(opens in new tab)](https://www.epa.gov/ghgemissions/global-greenhouse-gas-overview)
. And part of that is because electricity … the reason there’s that difference is …

**BURGER:**
You’ve got coal plants.

**LUERS:**
You’ve got coal plants, and it’s not as efficient when you do coal plants. You actually get efficiencies when you go right from solar to … in terms of just the energy because you lose a lot of heat in the thermoelectric plants, right? So there’s an efficiency there. But, so about 35% of the energy emissions are from electricity, and electricity production is really the key issue. You know, the key issue of today is, like, electricity
*and*
datacenters, right? How are you going to get enough electricity? How are you going to get enough clean electricity?

And that is something that is often more of an infrastructure problem than actually the energy problem. I mean, they’re both true. But it’s getting that electricity in the right location at the right time. And that’s sort of a big …

**BURGER:**
It’s a big messy problem.

**LUERS:**
It’s a big, messy problem that we can unpack a little bit. Because I do think there’s a role for AI, a huge role for AI.

**BURGER:**
Maybe even an optimization problem.

**LUERS:**
Maybe even an optimization problem. Exactly.

**MENACHE:**
Maybe.

**BURGER:**
We’ve got this guy in the room. This is exciting.

**LUERS:**
So we should unpack that. But I think before we go off that, just two points that I think are relevant. One thing is that, which is often not necessarily realized by people who don’t spend their lives … haven’t spent their lives thinking about climate, but to tackle the climate problem, we need massive amounts more of electricity. That is, that’s just part … I said we had 170,000 terawatts of energy. Most of that, to be able to solve the problem, has to come in the form of electricity because that’s what we can decarbonize easiest. So one of those challenges is actually
*more*
electricity.

**BURGER:**
Got it. So let me again try to break this down to a simple statement. So we’ve got, you know, about 35% of emissions are due to electricity use …

**LUERS:**
Thirty-five percent of energy emissions.

**BURGER:**
Thirty-five percent of energy emissions, which is three-quarters of the pie. So we can do the multiplication. And, of course, you know, as we decarbonize electricity, there is a probably too slow but ongoing transition towards a lower carbon emissions generation of electricity. You know, you convert a coal plant to a natural gas plant, it gets better. You put it to solar wind, it gets even better. But then the demand for electricity is going up, in part fueled by, you know, the tech industry and building the datacenters and AI, but in part because, like, we have to stop burning fossil fuels.

**LUERS:**
Right. Electric vehicles, turning all of our heating into electric heat—turning everything … the phrase is sort of electrify everything ahead of … the IEA, you know, says we’re in the era of electricity, right?

**BURGER:**
So, so we have a huge pressure on electricity demand. And we need to have it be, you know, low carbon electricity generation, but the demand is just going to go up and up and up with or without, you know, this datacenter buildout and this AI buildout. But, but of course this is happening, and the hope is we can use it to provide a lot of value.

**LUERS:**
Yeah. So there’s one other sort of context which is really important here, and that is that the other concerns that are being raised around this issue of electricity and datacenter growth is at that local community level, right?

**BURGER:**
Right.

**LUERS:**
So datacenters contribute a very small percentage globally in terms of emissions and even in terms of electricity, but they’re
*really*
concentrated. They’re one of the most concentrated industries in the world. There’s this great figure if you ever want to look up the recent
[IEA report on energy and AI
(opens in new tab)](https://build-up.ec.europa.eu/system/files/2025-04/PChtNmAZVk_11_04_2025_145800.pdf)
, which really shows the concentration of different industries, and steel’s way on one side, which uses 7% of the emissions, which produces 7% of global emissions. And datacenters are all the way on the other side, which are real in terms of the level of concentration, how close they are together.

And the reason that’s important is that there’s certain pockets of the world where there’s really a lot of datacenters, and they keep going into those areas. It’s changing a bit now because of the dynamics that are happening. But when that happens in the … then in those big … in those areas, yeah, they’re a major user of electricity, right. And when the growth happens quickly in
*those*
areas, then it can be …

**BURGER:**
It affects the local grid.

**LUERS:**
… then it can … it can put a strain on local grid. And so there are concerns that are being raised in certain regions in the world about datacenter growth. And, and you know, I’m really optimistic that those are mainly infrastructure problems, and they can be addressed.

And we need to figure out how to do that. And I’m really … that’s why I’m so excited about … in January, we
[announced our community-first infrastructure initiative
(opens in new tab)](https://www.linkedin.com/posts/amyluers_ai-sustainableai-sustainability-activity-7417061014812274688-FrDU/)
where we’re really focusing all of our work now on how do we design our datacenter development to ensure that that rapid growth is not a net negative, but actually a net positive for those communities. And that includes, you know, committing to paying all of the prices that it requires to meet our electricity needs so that our datacenters do not drive… prices increase in communities.

**BURGER:**
So I can see how we can get to a net level like, you know, we basically don’t drive up local prices …

**LUERS:**
Yeah.

**BURGER:**
…don’t exacerbate local water supplies and bring it in, however you can do that. But how do you make it a net positive?

**LUERS:**
Well, I think that, you know, we have been saying we’ve been net positive at a global scale, and I think we’re shifting that to say, what do we mean … what does it mean for net positive at a local scale? And I think at a local scale, for example, datacenter water use is,
for cooling, can go net positive in the sense that in the datacenters themselves, we are actually beginning to design systems that use essentially zero water for cooling.

**BURGER:**
Right. It’s recycling. Yup.

**LUERS:**
Certainly. So we can, you know, that isn’t in place everywhere, but there’s happening now.

And then we replenish water, so we can do things … so for example, it turns out in many places—water in some cities is lost with leaking pipes, and
[AI, it turns out, can help identify those leaking pipes
(opens in new tab)](https://news.microsoft.com/source/features/sustainability/ai-tool-uses-sound-to-pinpoint-leaky-pipes-saving-precious-drinking-water/?msockid=22be524939886e792aa2463938e76f45)
. So even if you get half of that, even if you save half of that, that can be way … our … the emissions from datacenters … the loss … the use of water in datacenters is only a fraction of what we would save. And so you can, you can amplify and save water oftentimes even by using AI, another optimization problem, in many ways.

**BURGER:**
So, so this is more of a, this is more of a commitment from the company to work with the community to get them to a better place. But of course, using our global compute because we’re not going to just run the AI analysis that makes the pipe better in the datacenter that that can be …

**LUERS:**
Oh, no, no.

**BURGER:**
Right. But we’re just trying to … yeah …

**LUERS:**
And it’s not just about … we’re not doing it just with AI.

**BURGER:**
Of course not. Of course not.

**LUERS:**
We’re also investing in training. We’re investing in NGOs. The real focus is to really understand what that looks like. And, you know, my interest is really to say, you know, can we increasingly co-design? What does community positive mean? This is all new because this rapid growth was the first time that this became such a serious issue of concern.

**BURGER:**
Right, right. Well, I’m really glad you’re pushing on this, and I think it’s really important for the communities because if, you know, if we can put enough focus and enough innovation to make these things a net positive, I’ll certainly feel a lot better about it.

Going back to the emissions. So one of the reasons I brought you both here today was because Amy gave a talk at our research showcase, which really inspired me. And you talked about a lot of the emissions being generated through things like transport and inefficient management of some of our large, you know, nondigital systems.

And I … I heard that and I’m like, wow, this might be a place where some of our research could help. And of course, that’s my job, right, is to find places where our researchers can amplify the effect of their work.

So, Ishai, maybe just very briefly, can you talk a little bit about when you worked with the supply chain and you applied your optimizations techniques. And this was even before OptiMind, where you know you could do scenario planning for natural language. What sort of efficiencies were you able to drive just working internally with our business teams?

**MENACHE:**
Yes, so I’ll give you a couple of examples, but starting off with what you mentioned about transport actually. So as part of this intelligent fulfillment service we are actually accounting for shipping costs. And one thing that one can do is account … also take more explicitly into account, you know, emissions and the sustainability considerations when doing the shipping itself, right? So that’s one kind of one option.

**BURGER:**
So we could say, like, get … have the same, like, level of risk and time to delivery, but as your objective just try to drive your emissions down.

**MENACHE:**
Correct.

**BURGER:**
As one example.

**MENACHE:**
Correct. There are other related examples of when, you know, what kind of hardware you use, when you have to fulfill the requirements, and for example, you want to use hardware that has been sitting for a long time in the warehouses. So that also has some implications.

Now, you know, we’ve worked over the years on various systems that, you know, efficiency has been a major goal of us, but sustainability is closely related to efficiency, and I can illustrate it through concrete examples.

So one is virtual machine allocation, which operates at a [very fast] time scale. It’s the process that essentially maps VM requests to physical servers.

**BURGER:**
That’s in our cloud, you know, …

**MENACHE:**
That’s in our cloud. Correct.

**BURGER:**
… when a customer wants to use something. Just again, we’re keeping it, like, not too geeky here.

**MENACHE:**
So one of our goals was to increase packing density, which means that we want to operate the servers close to 100% of utilization. And it is well known, actually, it’s a
[study by Google
(opens in new tab)](https://ieeexplore.ieee.org/document/4404806)
. I guess you’re familiar with it. Actually, you know, as you increase packing density, actually you reduce the power per unit of useful compute, right? So that’s well known. So for example, I don’t remember the exact numbers, but if your server is utilized at 50%, you still consume, like, close to 100% of the power.

**BURGER:**
Yeah, you’ve provisioned it. You know, it’s being transmitted. You know, your chips leak, they have static power dissipation, all the stuff, sort of stuff I used to work on.

**MENACHE:**
That’s actually … Doug knows better than me for sure. You know that’s been his area of research.

So another example that we’ve worked on since 2022 is rack placement. So you have these demands, and you have to decide how to exactly place them, these racks of servers within the datacenters. And there you have to account for power and cooling and, you know, space, and all that. And one of the things that we were able to achieve with our optimization is reduce power fragmentation by 1 to 2%.

So 1% here is huge, you know, and it’s not only about, you know, the cost savings, the money savings for the company, but it’s also about, you know, having to build less datacenters or utilize the datacenters in a more efficient way. And essentially another way to view that is that, you know, if we want to have AI … we want to have AI consumed by everyone in the planet, right? So essentially, you’re making it more kind of … with less, you can do more and have AI … you know, broaden the reach of AI and having it consumed by, you know, eventually all the world.

**BURGER:**
I mean, I think, I think internally in the company and with research and working with our product groups, you’ve been very successful because you’ve, you’ve figured out a bunch of ways in supply chain and in one of our largest businesses to make things run more efficiently, which is great, right.

And, you know, but to the people in the rest of the world, they care, like, you know, is the planet on a sustainable trajectory, right? You know, are their electricity bills going up? And, you know, we’re doing it under competitive pressures to improve our operating margins, which is great for us, …

**MENACHE:**
Right, right.

**BURGER:**
… but we have to think about the world. So, but I think there’s … we have something we can do here.

So now going back to Amy for a sec. In your talk, you talked about, you know, a lot of these emissions and opportunities. Are there a few big buckets you think we can tackle by just being smarter about how we manage complex systems? And what do you think the magnitudes are?

**LUERS:**
Earlier I said I don’t think we can actually solve the climate crisis without AI. And, and I think there are three game-changing capabilities that I see AI really brings to the sustainability process. And I … and one of them is this ability to enable, the way I think about it is, optimization but also understanding and predicting complex systems that we had a hard time doing with or it’s really impossible to do with the traditional analytical tools that we’ve had.

**BURGER:**
Right, right.

**LUERS:**
And the other game-changing capability is the acceleration of discovery, development, and deployment of new climate solutions. And that’s also of course another area that MSR does a lot of work in.

**BURGER:**
Right.

**LUERS:**
And the third game-changing capability that I see AI brings to sustainability is the ability to enhance and augment institutional human and workforce capacity.

And I think all three of these are important and can be game changers if we lean into them. In the context of specifically the managing of optimization or the optimization of complex systems, I think, you know, the biggest challenge that we really have to do is, as I said, transfer … electrify everything, right? And that has many levels of where optimization fits in
*and*
accelerating discovery fits in
*and*
the third green path. Like, it has various different levels, but one piece is infrastructure.

So the IEA
[projects
(opens in new tab)](https://iea.blob.core.windows.net/assets/4719e321-6d3d-41a2-bd6b-461ad2f850a8/NetZeroby2050-ARoadmapfortheGlobalEnergySector.pdf)
by 2050, to get net-zero by 2050, which is the global climate goals, at a global scale, we need to more than double the electricity capacity of the world. I mean, now think about that. That’s a, that’s a big undertaking.

And so increasingly, that ability to be able to integrate and manage a system while the climate’s changing and the weather’s becoming much more predictive, that becomes a challenge that if we get it right, we can integrate more. And if we don’t, we’re going to be really going very slowly towards that goal.

**MENACHE:**
Yeah, I want to actually …

**BURGER:**
I saw you twitching in your seat.

**MENACHE:**
Yeah, yeah. So we were talking a lot about optimization, but there’s also the AI itself that helps along the way to make systems more efficient. And, you know, what we do a lot in the team is actually combining AI prediction techniques with optimization, and that is very powerful. And I’ll give a couple of examples. So for example, in the virtual machine allocation set of problems, so what we did, we actually, you know, we predict the lifetime of the VM. Like, how long do we think that the VM will stick in the system?

So there are kind of AI, complementary AI systems that do this prediction for us, and that produces a more … better optimization. When you have, like, intuitively, when you have more knowledge or sort of …

**BURGER:**
Better predictions.

**MENACHE:**
… better predictions. It doesn’t have to be super accurate, but as long as you have, like, decent predictions, you could do much better with packing. So that’s one example. And, you know, in the context of cloud supply chain, predictions, demand predictions, are critical because if you have very bad predictions, then you need to sort of provision ahead. Like, we talked about this, that you have to sort of …

**BURGER:**
You have to buffer capacity, you have to build extra capacity in the system, you’ve got redundancy—it’s expensive.

**MENACHE:**
Right. You don’t know what’s going to happen. So, you know, optimization helps you automate and find the sort of optimal choice. But if your demand predictions are bad, you’re going to have to provision, overprovision these hot buffers. And that also has an environmental effect as well as, you know, cost implications. So I think this kind of blend of AI and optimization, this is something that we are really, I think, really is going to kind of drive things forward.

**BURGER:**
I want to be a little careful here because, you know, we … there’s a lot of excitement about this technology because it’s so disruptive. And, you know, for people listening, you know, I’m an anti-hype guy. Like I used to like to work in areas that were not hot because, you know, communities would get over excited about stuff. But the stuff we’re seeing these advanced models able to do is just jaw-dropping. And, and it is … the capabilities are actually moving really fast.

But those can have bad consequences for society too. I mean, you know, the internet had a set of consequences. Social media had a set of consequences. You know, we are on an unsustainable path right now, trying to get on a sustainable path. And that’s not all tech, that’s just human civilization.

So I really want us to focus, maybe dream a little bit now, like what are the places we can try to steer this tech, you know, AI and all of this compute, to solve some problems that really move the needle for the climate. Because my own hope and goal, and I think, Amy, we probably share it, in fact, I think we all do, is as technologists, you know, steer the technology in a way that helps people in humanity and overcome some of the bad effects because, you know, we’re going to get both as with any new technology.

So like, should we be managing cities with this stuff? Should we build models that just control the grid? Control not in a sense of like, you know, just are able to optimize. Like what are the things we could do five years out, two years out that might be magical and would really move the needle.

**LUERS:**
So …

**BURGER:**
You had your three.

**LUERS:**
Yeah.

**BURGER:**
So maybe we can bucketize it in those.

**LUERS:**
Well, I had three game-changing capabilities. So I would put those game-changing capabilities on problems. Right. So first is, this is what—when I look at AI—are the things that you can put on a lot of climate challenges, sustainability challenges and really make huge differences. And then the question then is, well, what are the three big challenge areas, right?

**BURGER:**
Right.

**LUERS:**
There are a lot of challenge areas. I guess in terms of— we can unpack these—but at the high level, I would say, we’ve already talked about this, but the first one is, you know, enabling electrifying everything, and there are various bullets under that. The second one I would say … I would highlight industrial materials and chemicals, and that’s a discovery-development-deployment type of thing. And it’s packaged like all of these. You can’t just sprinkle AI and it solves the problem, but it can make …

**BURGER:**
It’s real work.

**LUERS:**
It’s real work, right? But I think that there’s a different model in the second bucket of industrial materials and chemicals. I think the thing that I really at least envision that there’s a different way of approaching that
*because*
AI exists, and we can unpack that if you like.

And the third one, I would say, is building … enabling the development of a low carbon and resilient secure food system.

**BURGER:**
I see.

**LUERS:**
Food system counts for, you know, about one-third of emissions. And it’s also one of the biggest impacts of climate change itself. One of the issues of vulnerability and food insecurity is a huge issue.

**BURGER:**
Is this fertilizers?

**LUERS:**
It’s fertilizers. It’s also …

**BURGER:**
Water …

**LUERS:**
… like methane in terms of cows, …

**BURGER:**
Methane emissions …

**LUERS:**
… it’s in terms of, you know, and also how we grow food and how we distribute it in terms of supply chains. There’s …
[food waste is about 8% of emissions
(opens in new tab)](https://unfccc.int/news/food-loss-and-waste-account-for-8-10-of-annual-global-greenhouse-gas-emissions-cost-usd-1-trillion)
. So there’s a huge amount of inefficiencies. And again, I think the three game-changing capabilities can … there are ways that it can impact each one of those three buckets.

**BURGER:**
Within MSR, we, just in the last month, you know, we’ve had teams design a better X, where X was this percent more efficient using, you know, genetic algorithms or neuroevolution.

You know, these aren’t LLMs, but LLMs, you know, can play a role in this. And I wonder if we were going to go tackle a set of problems, you know, so Ishai’s work could think about taking large, complex systems and figuring out how to run them more effectively. And I think what you’re saying is, could we, you know, could we design a better wind turbine that would generate more electricity, you know, for a given wind speed or just through optimization or …

**LUERS:**
Well, I mean, I think that that would be …

**BURGER:**
… materials, like, for direct air capture, carbon capture. What would be on your list?

**LUERS:**
Yeah. I think in the context of materials, you know, some examples, I mean, of course, cement. Some of the materials, a lot of the issue is tied to electricity. So it’s the optimization of the process. So for steel, for example, you know, a lot of that is what energy you use to do it and how you can optimize that
*system*
.

But there are also lots of different materials that can make processes more effective, you know, materials for desalinization, would reduce a huge amount of electricity, and that also connects to this vulnerability and security piece, you know, which I said is a threat.

**BURGER:**
Potable water would be huge if you could do it with low energy.

**LUERS:**
Yeah, yeah, and so the way, you know, one of the things that I have sort of dreamed about is like it couldn’t now … we used to have these challenges, these like grand challenges that, you know, were decades long, that we would have moon shots. And I feel like if we focused AI on different challenges and said, let’s think about those grand challenges in the areas that are really focused where AI can make a difference and say, let’s think of them as like factory moon shots. In other words, like, let’s just say we are going to set up a system to be able to … what are the 10 materials that if we solved and addressed it would really make a difference in energy and food and all the … in society.

**BURGER:**
We need this list.

**LUERS:**
And kind of check them off. You know, like just … and get public-private partnerships to also do that together. And then you have to prepare, though. You have to prepare alongside to be able to have that system so that they can move into society, right.

**BURGER:**
That’s exactly right. And I’m, you know, I was going to pull up my, you know, pull up a
[paper](https://www.microsoft.com/en-us/research/publication/closed-loop-optimization-using-machine-learning-for-the-accelerated-design-of-sustainable-cements-incorporating-algal-biomatter/)
here. Kristen Severson, who’s at MSR, and three of her colleagues at the University of Washington—I think you know about the work—you know, used a form of machine learning, you know, Markovian processes, to design cement that used … that had algae in it, but is as strong and generates 20% fewer carbon emissions. Now cement is a huge chunk. I don’t remember what it is.

**LUERS:**
It’s about 7%, 6 to
[8%
(opens in new tab)](https://www.weforum.org/stories/2024/09/cement-production-sustainable-concrete-co2-emissions/)
, depending how you measure it.

**BURGER:**
Yeah, so you chop a fifth off of that, and all of a sudden that’s 1 to 2% … between 1 and 2% of emissions. But of course, you know, and it looks like it will be as strong and have all the right properties. But getting it from the paper, you know, in
*Cell*
to wide-scale production across the world is a huge undertaking.

**LUERS:**
Totally

**BURGER:**
So, you know, we can solve these problems locally, but then getting them to scale, especially when you’re working in a company that doesn’t produce cement, like how do you do that? That’s a, to your point …

**LUERS:**
Right. That’s why you need it… you need to do this as a public-private partnership. Like this should be thinking about it in terms of, we are going to have a mission to get 10 of these in the next however many years, not trying to just have a moon shot for one in the next several decades, right?

**MENACHE:**
So my list is, like, so number one is everything that Amy said, like …

**BURGER:**
That’s a long number one. [LAUGHTER]

**MENACHE:**
Yeah. So, no, but I should say one of my mentors said like every problem probably has some operation research, OR. You know, when you’re standing in a line, at McDonald’s—that’s where he said it to me—you know, to take this queue or that queue, you know, and like, you know, when you stand in line. So that’s how he was thinking.

But you know, to the point, I think domains that you described, you know, materials, food distribution, electricity, there’s a lot there to, sort of, that we can contribute as optimizers. And in fact, I think we can do a little bit more when it comes to concretely kind of accounting for sustainability metrics. I mean, we talked about that. You know, taking into account more explicitly renewables and such. So I think there is some way to go there.

Number two, I think that, you know, optimization and AI can be used for humanity, for well-being. I’ll give one example. There are all sorts of scheduling systems, and it’s actually a project we started looking into. You know, how do you, sort of, make the system more efficient? You know, you want to reduce cost, but still account, for example, for labor laws and, you know, prioritization on or, you know, union kind of considerations.

And AI can help with that, you know, to actually understand the contracts and understand the fine prints and come up with an algorithm, scheduling algorithms, that are good also for, you know, for the people, right. So it’s, like, you know, for example, if you take into account how many hours drivers, you know, they have this kind of long shifts. How can you sort of prioritize that they have enough rest and account more explicitly for their well-being? So that can be done with a combination of optimization and AI.

Lastly and importantly, I would say, you know, part of the premise and, like, the vision of
[OptiGuide](https://www.microsoft.com/en-us/research/project/optiguide-genai-for-supply-chain-optimization/)
, which is the project that we’ve been working on in the intersection of gen AI and optimization
[[1]](#_ftn1)
, is making all these kind of complex, you know, tools that we have for making better decisions … and by the way, it’s not only, like, I gave an example of, you know, optimization algorithms, integer linear programming, and all that, but it’s not only that. Think of like very advanced simulation tools that you have also in the electricity space when you model greed and stuff like that. Make them more accessible to end users, to planners, business operators and executives that have to make decisions. So I think that’s also something quite important here that, you know, AI can help facilitate.

**BURGER:**
People, humans get, we get very comfortable with rapid change as long as the change stops. Like we can ingest, you know, if a second moon appeared in the sky, everyone would look at it be like, oh my god, there’s a second moon.

And a week later it’d be like, yeah, there’s two moons. And that’s just how it is, right? And we normalize to it. And so we all think that the society we live in right now is normal, but it is a historical anomaly, you know, exponential population growth, agriculture, industrial revolution allowing a massive increase in population. And our whole economic model is sort of based on exponential population growth fueled by unsustainable fossil fuels and resources. Like, that’s our standard of living. And a big chunk of the world is still really poor.

So I think we have to move to something different, and maybe we just get to this … enough materials to a sustainable future. But to your point, you know, it’s not just about efficiency because these are human beings. These systems we build have to factor in human well-being. And that’s incredibly complex. You can’t do it with, like, a bespoke regulation, you know, regulations hard, policies hard. So my dream is that we can use these very complex systems to kind of evolve and learn that balance. Like, can we actually manage society and its complexity in a way that fulfills the human condition? I don’t know if it’s possible, but it’s, you know, we’re fighting this fight, and it’s really tough.

So I guess for me that’s my hope. I, you know, Amy, you have dedicated a big chunk of your professional life to this topic. Like, what is your aspiration? Like, what would you like to solve? If there’s a problem we could solve in research, what would it be, like kind of what, what would you really like to see happen? What’s your dream?

**LUERS:**
Well, I think to answer that, I’d like to put a twist on your vision of that in terms of … because the way I see it is right now we have built over the years a society that’s based on a broken system. We have, you know, fossil fuels at the bottom, and broken infrastructure and inequities in the world.

**BURGER:**
Massive.

**LUERS:**
Massive inequities in the world. And so right now, anytime we, like put a new thing on that system, it just creates more emissions, draws more problems because we have the same model that we’re doing.

**BURGER:**
Right.

**LUERS:**
The unusual thing about AI and the reason I think it’s so promising and so scary is that it’s the first time we have a tool with such power that can actually change that system that we’re built, we’re based on if we use it to do that.

**BURGER:**
Yes.

**LUERS:**
And so, you know, I think we need to focus it on those things. I’ve written about, you know, five and now it’s become six, but I’ve written about sort of five things that have to happen for us to be able to direct it to change that system.

And the first is, yes, we have to use AI for sustainability, right. I know that sounds sort of trivial, but it’s not trivial because everybody often says, well, there’s a lot of potential out there. And I’m like, yeah, well, the climate crisis, solving the climate crisis is figuring out the potential and then making that a reality.

The second is data infrastructure, and the data and data infrastructure to be to be able to solve these problems.

There’s a lot of … we have to get that data out there right. The third is making access to clean energy and reducing our footprint and supporting communities. Like, those I think are the infrastructure side of it.

**BURGER:**
OK.

**LUERS:**
The next one is what I call governing AI for Earth alignment. And we, with colleagues from around the world, have written… we wrote a
[paper in Nature Sustainability](https://www.microsoft.com/en-us/research/publication/the-earth-alignment-principle-for-artificial-intelligence/)
that sort of outlines this vision of what it means to have Earth alignment in AI in principle. And I think that’s another one. And then the fifth is to skill … upskill the world, like, you know, you said, make it more accessible.

Some of it’s not necessarily learning how to, you know, build agents, it’s being able to, how to understand how do you integrate these tools into your life in a way that actually can drive this change. And I would add one other—and probably is closer to number three than to be in the sixth—but I do think we need to figure out not just [how] to work with communities, but to align the development of datacenters and AI operations with the needs and the trajectory of the electricity grid. And I think that’s not just applying AI to solve solutions through optimization but also thinking about this in an integrated way.

**BURGER:**
Yeah. Ishai, you have a response, and then I have a question for you.

**MENACHE:**
Yeah. So oftentimes decisions are made by multiple parties, right.

So and, you know, each party makes substitutive decisions, and there’s also, you know, they affect what others have to … can decide. Like they change essentially the settings for others that make decisions. So there is kind of dependencies between decisions that I make and decisions that you can make.

And I think that AI can also help sort of can be the glue in this very compound, very complicated systems where there’s, like, distributed decision making. And I think with AI, with all this kind of agentic sort of workflows, we can, you know, take into account moralistic considerations. So obviously in the energy space, as well. So I see a lot of potential in kind of solving for real problems without making too many discounts or, you know, just saying like, you know, I’m focusing only on my, you know, small world. With this kind of combinations of advanced analytics and AI, we can actually get much further with moralistic and more global optimizations that are good for society.

**BURGER:**
How do we take all of that and putting all of these decisions and, you know, complex systems and infrastructure and balancing and put it under control of these massive computational structures that learn things that are now too complex for us to understand and retain human agency?

**MENACHE:**
Yeah. I mean, that’s a tough one. I wasn’t expecting this question. [LAUGHS]

**BURGER:**
Oh, my next one’s worse. [LAUGHS]

**MENACHE:**
We’re out of time. [LAUGHS]

You know, I feel that, you know, there’s not a perfect answer here, but I think that explainability of these systems, of these sort of complex systems, is part of what AI can unlock. So you’re getting these outputs, but you know, as a user of AI, you can also ask questions of like, why? And that’s actually something we’ve been really focusing on in cloud supply chain management is like, you know, why are these decisions being made? Can you just explain to me the alternatives? So actually, with AI, you can explore alternatives quite fast and, you know, having this natural language kind of interface, and then you can get better understanding why certain decisions have been made.

**BURGER:**
Yeah. Ishai, you know, you’re one of the top experts, you know, in optimizing complex systems. You’ve done phenomenal work, and I’m really proud of the work you’ve done and the impact it’s had. Do you have a dream? Like if your work could scale to solve some problems or do something intellectually beautiful, like, would you like … when you look back on your career and you achieved X, you know, what would that be?

The problems now are so important, and there’s so much that can be done. And you’re right in the center, I think, of what’s possible.

**MENACHE:**
You know, I think the dream is to get into areas which we thought that were impossible, like, a few years ago. So like,
*no, this is not a place where some of your expertise—that’s not for you.*
…

**BURGER:**
Yeah.

**MENACHE:**
*This is, like, you know, there’s legacy, and there’s, like, you know, it’s just too complicated.The data is not in one place.*
And all that. So we did a little bit with the supply chain, which is, you know, a big challenge there is data.

So I would say, you know, at least from a technical perspective, you know, using AI optimization, advanced analytics to essentially create a unified decision intelligence platform, where the sky is the limit, where you have maybe multiple decision making, multiple considerations. You don’t even know when you start what all these considerations are.

So like having, like, a more interactive system that optimizes in a continuous form. And, you know, one aspect of that is also, which is I think a big challenge, is all these black swan events, rare events, that, you know, optimizations, it’s hard for them to, you know, account for.

So, you know, how do we kind of incorporate optimization in real time and have it reactive and maybe, you know, with a bit less human in the loop, but the human is still an important part in, at least for the foreseen future, in verifying these outcomes and being confident about them. And I would add to that also a part of it is, like, educating humans that are not, like, maybe do not have the same, you know, level of expertise in certain areas.

That’s another thing that we have to think of. How do we explain to humans that, you know, have something to do with the business? How do we explain to them and make them feel comfortable about what the system underneath with all these AI and all these complexities are doing?

**BURGER:**
I, you know, I was listening to it, and it’s really, it’s a beautiful answer actually. And it’s really compelling. I’m going to try to restate it.

Number one, take any system that you can define, no matter how complex, and drive it to near optimal for some criteria—for emissions, you know, managing an energy grid, for example, or how much renewable capacity to provision, or which problems should I … so that, like, if you can achieve that, right, then humanity has an amazing tool to just make … squeeze all of this waste. You know, we talk about, like, wasted food. That’s a massive target you could go after. So just that capability, any system can be brought to near optimal. We just have to define it and then pick one.

And then the other one I loved is how do you plan for resilience if you can speculate on a few of these black swan events? We know that these things are going to keep happening, and they’re going to get worse.

And we’ve seen the hurricane in Jamaica, right? And we just, you know, and North Carolina, and there’s just … so how do we build societal resilience with these rapid changes? That’s an optimization problem.

**LUERS:**
Well, but that’s an interesting question. I would wonder what both of you think about is that, I mean, I think there’s, there is a world that thinks that optimization and resilience are not necessarily always compatible. And so, you know, there is a world where, you know, and I … that resilience and … redundancy in nature is about resilience. You know, that is part of the resilience of these systems. The complexity …

**BURGER:**
There’s a reason why we have two kidneys. [LAUGHS]

**LUERS:**
Yeah, and so, you know, I think a lot about the resilience of ecological systems and, you know, and there is a lot of concern about that. When you optimize it, are we actually making ourselves less resilient? I’m just curious. I know we’re running out of time, but as this tension came up, I was wondering what you guys have thought about that in terms of, you know, how we can move forward with these tools in that space.

**BURGER:**
Well, I’ll jump in there and then turn it over to Ishai. I mean, having designed, you know, with my team, large scale systems that have to be, you know, resilient, you also don’t want massive replication. So there is an art to figuring out where do you over-provision, and how do you do it intelligently so that you get, you know, given some model of failures and byzantine problems like the right outcome. And so, you know, resilience can be just: I’m going to put a ton of food and water and fuel everywhere in case something happens. But you can also be really smart about it. So it really is an optimization problem.

**LUERS:**
But you need resilience in your criteria for optimization.

**BURGER:**
That’s right. You need to know what you’re predicting for and what you’re trying to solve. And then you optimize. And that’s what I was trying to say to Ishai. You optimize around that.

**MENACHE:**
So my first answer was more like Doug’s, is on the system side. And definitely resilience is being accounted for, you know, durability, and also things …

**LUERS:**
Yeah.

**MENACHE:**
… in certain systems, storage systems and such, things that Doug has worked on for many years. I should say that more on the supply chain side and optimization side, it’s a big topic, resiliency.

**LUERS:**
Yeah.

**MENACHE:**
And, you know, and optimization can capture in a formal way measures of risk, right. So you’re not, like, optimizing … necessarily optimizing for the average outcome, average profit, average cost. But you can take into account explicitly risk measures when you’re optimizing, like, value at risk, and other measures that explicitly account for risk. And there are other ways in optimization that you account explicitly for uncertainty, stochastic optimization, where you try to model the uncertainty in the form of, in a distributional form, robust optimization.

Maybe you don’t have the distributions, but you still have some sort of polytope of possibilities in the world, and you just kind of, and you do it … actually network routing, for example, you’re saying like, I don’t know exactly where I’m going to be, but I’m optimizing in a way that no matter where I am, what the state is going to reveal to me, I’m going to do quite well, right.

So there are ways to account for that again, depending, and what I said about AI is that, you know, again, a supply chain planner, a network operator, they might not be familiar with these formal terms.

**LUERS:**
Right.

**MENACHE:**
So how can we make it more accessible to them? Like they have to define the objective now. They know that they have some risk that they want to account for. You know, how do we sort of help them formulate it in a way that is commensurate with what they actually need?

**LUERS:**
Yeah.

**BURGER:**
Amy, you look like you want to weigh in, and then I’m going to bring us to a close.

**LUERS:**
I guess I was thinking that this is the area … you had asked about human agency and this idea of human in the loop to not having automatic. But there’s also another side of it—of how you could have these systems potentially help not just focus on optimization
*without*
thinking about resiliency. You know, …

**BURGER:**
Right, right.

**LUERS:**
… if you embed that in the system, then it might have this two-way influence that could have a net benefit.

**BURGER:**
Hundred percent.

**LUERS:**
So, you know, that’s something I think that’s a really interesting area to pursue.

**BURGER:**
I can tell you both that if I were listening to this podcast after hearing the discussion … and I want to thank you both. This was really fun, and I learned a lot today, which is great.

**LUERS:**
Yeah, I did too.

**BURGER:**
I didn’t have somebody saying
*polytope*
on my bingo card this morning when I got up. … I would be really curious and maybe even a little bit antsy to see what is that list of those top problems, priorities, and then from you because you talked about it. And so maybe if at any point you get it, I’ll post it along with this. And then which one does Ishai pick up and start working on?

**MENACHE:**
Yeah, let’s talk. [LAUGHTER]

**BURGER:**
You know, it would be great to have some positive outcome. So if we do get the list, if you do pick up one of these and make progress, you know, I would love to report out to people. And I’m hoping, you know, the ties we made today and the discussion we had lead to something like that, …

**MENACHE:**
Absolutely.

**BURGER:**
… that makes the planet better.

**LUERS:**
Excellent.

**MENACHE:**
Thanks a lot.

**LUERS:**
Thanks so much for having us.

**MENACHE:**
It was lots of fun.

**BURGER:**
This was really great. Thank you both.

**MENACHE:**
Yeah, thank you.

**LUERS:**
Great.

[MUSIC]

**STANDARD OUTRO:**
You’ve been listening to
*The Shape of Things to Come*
, a Microsoft Research Podcast. Check out more episodes of the podcast at
[aka.ms/researchpodcast
(opens in new tab)](http://aka.ms/researchpodcast)
or on YouTube and major podcast platforms.

[MUSIC FADES]