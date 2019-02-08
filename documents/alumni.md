<h2>Senior Research Associates</h2>
<ul>
 	<li><a href="http://markring.com/" target="_blank" rel="noopener">Mark Ring </a></li>
	</ul>

<h2>Research Associates</h2>

<ul>
{% for af in site.data.people %}
{% if af.alumni ==  'research associate' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
{% if af. status %}
	 ({{ af.status }})
{% endif %}	
	</li>
{% endif %}	
{% endfor %}
</ul>


<h2>Post-Doctoral Fellows</h2>

<ul>
{% for af in site.data.people %}
{% if af.alumni ==  'postdoc' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
{% if af. status %}
	 ({{ af.status }})
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>
	
<h2>Ph.D. Students</h2>

<ul>
{% for af in site.data.people %}
{% if af.alumni ==  'phd' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
{% if af. status %}
	 ({{ af.status }})
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>


	
<h2>M.Sc. Students</h2>

 <ul>
{% for af in site.data.people %}
{% if af.alumni ==  'msc' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
{% if af. status %}
	 ({{ af.status }})
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>
