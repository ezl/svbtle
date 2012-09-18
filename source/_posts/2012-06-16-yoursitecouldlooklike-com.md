---
layout: post
title: YourSiteCouldLookLike.com

---

My old gym has a website that renders terribly on mobile, yet everybody at the gym goes to it every day to see the workout (that may sound weird, just trust me that it's a typical crossfit gym thing).

Everybody goes to the site every day to see ONE thing: the workout of the day.  Then you get there and have to pinch and zoom to read it.

I want a mobile version. So I threw together my own stylesheet for it. It'd be great if I could show my friends.
<h2><strong>Somebody Please Build This</strong></h2>
<strong>http://yoursitecouldlooklike.com</strong>

"Your Site Could Look Like" is a website. Sort of like <strong>bitly, but it doesn't just redirect, it loads the target page AND adds additional stylesheet rules</strong> to it. Basically, it lets you apply any css to any website and show it off to your friends (or the customer who you are trying to woo).

<h2><strong>How it works</strong></h2>

On the main page there are 2 input fields and a submit button.
<blockquote>
<div>1) Target Site URL:</div>
<div>2) CSS file location:</div>
<div>3) [Submit button]</div>
</blockquote>

User puts in a website and an alt stylesheet for it. On clicking submit, they get back a unique url:

<blockquote>
<div><strong>http://yoursitecouldlooklike.com/xT6j2</strong></div></blockquote>

Set up an nginx/apache reverse proxy. Whenever someone accesses that URL, the service curls the target site (1), inserts the contents of the CSS file immediately before the closing html tag (2), then serves the page to the customer.

If you want to be fancy, you can count page views, do analytics on the ip addresses that access it, etc. You can also let people insert their own js file. Will someone build this please?
