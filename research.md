<h2>Research Projects by Topic</h2>

<ul>
 	<li><a href="projects/offpolicy.html">Off-policy policy evaluation</a></li>
 	<li><a href="projects/stepsizes.html">Stepsize selection</a></li>
</ul>

<h2>Publications by Year</h2>

<!-- Super important: do not indent the content line, because then it -->
<!-- gets treated like code -->
<!-- Old stuff now, Alex has a better suggestion
{% assign sortedyrs = (site.publications | sort: 'name') | reverse %}
{% for pubyr in sortedyrs %}

<h3>{{ pubyr.name }}</h3>

{{ pubyr.content | markdownify }}

{% endfor %}
-->

{% for yr_hash in site.data.publications %}
{% assign yr = yr_hash[1] %}

<h3>{{ yr.yearname }}</h3>

<ul>
{% for pub in yr.pubs %}
<li>
{{ pub.title }}. {{ pub.authors }}. <i>{{ pub.conference }}</i>, yr.yearname.
{% if pub.pdf %}
<a href=" {{ pub.pdf }}">[pdf]</a>
{% endif %}
</li>
</br>
{% endfor %}
</ul>

{% endfor %}
