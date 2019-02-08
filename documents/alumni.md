## Alumni



<h2>Research Associate Alumni</h2>

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


<h2>Post-Doctoral Fellow Alumni</h2>

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
	
<h2>Ph.D. Alumni</h2>

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


	
<h2>M.Sc. Alumni</h2>

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
