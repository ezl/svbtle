---
layout: post
title: 'Tracking HTTP Referer To Determine True Customer Lifetime Value'
categories: [rocketlease, code, strategy]

---

I want to be able to know what site referred users to my site.

More specifically, I want to be able to look back in a month, and say "users from Linked In did X over their next 10 visits."
<h2>Doesn't Google Analytics do that?</h2>
Not really. Google Analytics, as far as I know, will tell me where a user came from for a visit, but won't let me tie all the future behavior of the site user to their original referer.
<h2>Why Is That Important?</h2>
<a href="http://www.rocketlease.com">Rocket Lease</a> has different types of users. Small landlords, big landlords, property managers, leasing agents. While they interact with the site in similar ways, the strategy for connecting with each class of users differs and (I suspect) the total lifetime value of each customer class will vary.
<p style="text-align: center;"><a href="http://www.rocketlease.com"><img src="/images/rl2-300x156.png" alt="" width="300" height="156" /></a></p>
For example, I intend to advertise on various landlord and property manager forums. Professional property managers tend to manage more properties than a landlord owns, so they likely have higher lifetime value (LTV) and I might be willing to pay more per property manager conversion.

I need to know how much time/effort/money to allocate to advertising on Property Manager Forum X vs reddit/r/smalllandlords.

If there's a real difference in LTV based on user class, measuring global user LTV is a surefire way to inefficiently allocate advertising dollars.
<h2>Just a Little Bit Of Middleware</h2>
I had (still have) a nagging feeling that I was solving a solved problem, but I couldn't find someone else who had done it, so here's what I did.

<pre class="code"><code>
# 2 space indent because my blog is skinny
class OriginalRefererMiddleware(object):
  def process_request(self, request):
    referer = request.META.get("HTTP_REFERER")
    host = request.META.get("HTTP_HOST")
    path_info = request.META.get("PATH_INFO")

    if not "ORIGINAL_HTTP_REFERER" in request.session.keys():
      request.session['ORIGINAL_HTTP_REFERER'] = referer

    if not 'ENTRY_PAGE' in request.session.keys():
      request.session['ENTRY_PAGE'] = host + path_info
</code></pre>

<br />

HTTP requests come with a HTTP_REFERER header that me what page the user clicked through from. So if a user ends on my landing page from linked in, if I extract the HTTP_HEADER, it'll say linked in. But then if they go to my FAQ, now the referer is "<strong>rocketlease.com</strong>", then if they sign up from there, the referer will be "<strong>rocketlease.com/faq</strong>".

Instead, the first time (and only the first time) a user lands on any page served by me, I save the value of the referer. Then when the user finally registers, I just dump the original_referer to my database so at any future time I can determine how any user originally arrived at my site.

I'm planning on experimenting with LinkedIn, Facebook, and Bing ads in the next 2 weeks, so hopefully this will help me determine where I should be allocating ad spend. Linked In and Facebook in particular make it possible for me to target certain classes of users. Rocket Lease basically never makes an actual sale on the initial interaction with a user, so using the ad services' built in analytics isn't sufficient to determine value of a customer class.
