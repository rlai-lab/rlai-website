<h2>Research Projects by Topic</h2>

<ul>
 	<li><a href="projects/offpolicy.html">Off-policy policy evaluation</a></li>
 	<li><a href="projects/stepsizes.html">Stepsize selection</a></li>
</ul>

<h2>Publications by Year</h2>

{% for pubyr in site.publications | sort: "name"  | reverse %}

    <h3>{{ pubyr.name }}</h3>

     <p> {{ pubyr.content | markdownify }}</p>

{% endfor %}

