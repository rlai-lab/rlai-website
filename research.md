<h2>Research Projects by Topic</h2>

<ul>
 	<li><a href="projects/offpolicy.html">Off-policy policy evaluation</a></li>
 	<li><a href="projects/stepsizes.html">Stepsize selection</a></li>
</ul>

<h2>Publications by Year</h2>

{% assign sortedyrs = site.data.publications | sort %}
{% for yr_hash in sortedyrs reversed %}
{% assign yr = yr_hash[1] %}

<h3>{{ yr.yearname }}</h3>

<ul>
{% for pub in yr.publications %}
<li>
{{ pub.title }}. {{ pub.authors }}. <i>{{ pub.conference }}</i>, {{ yr.yearname }}.
{% if pub.pdf %}
<a href=" {{ pub.pdf }}">[pdf]</a>
{% endif %}
</li>
{% endfor %}
</ul>

{% endfor %}
