<h2>Research Projects by Topic</h2>
<ul>
 	<li><a href="projects/offpolicy.html">Off-policy policy evaluation</a></li>
 	<li><a href="projects/stepsizes.html">Stepsize selection</a></li>
</ul>

<h2>Publications by Year</h2>

{% assign yrfiles = site.html_pages | where: "arepubs", true %}

{% for pubyr in yrfiles | sort: "name"  | reverse %}

        <h3>{{ pubyr.name }}<\h3>

           {% include pubyr.path %}

{% endfor %}
