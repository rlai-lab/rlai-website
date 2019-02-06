<h2>Principal Investigators - Faculty</h2>
<ul>
 	<li><a href="http://webdocs.cs.ualberta.ca/~sutton/index.html" target="_blank" rel="noopener">Rich Sutton</a></li>
 	<li><a href="http://marthawhite.ca">Martha White</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~dale/" target="_blank" rel="noopener">Dale Schuurmans</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~szepesva/index.html" target="_blank" rel="noopener">Csaba Szepesvari</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~bowling/index.html" target="_blank" rel="noopener">Michael Bowling</a></li>
 	<li><a href="http://www.ualberta.ca/~pilarski/">Patrick Pilarski</a></li>
 	<li><a href="http://adamwhite.ca">Adam White</a></li>
	</ul>


<h2>Associated Faculty</h2>

<ul>
{% for af in site.data.people %}
{% if af.status ==  'faculty' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>


<h2>Research Associates</h2>

<ul>
{% for af in site.data.people %}
{% if af.status ==  'research associate' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>


<h2>Post Doctoral Fellows</h2>

<ul>
{% for af in site.data.people %}
{% if af.status ==  'postdoc' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>


<h2>Students</h2>

<h3>Ph.D. Students</h3>

<ul>
{% for af in site.data.people %}
{% if af.status ==  'phd' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>

<h3>M.Sc. Students</h3>

<ul>
{% for af in site.data.people %}
{% if af.status ==  'msc' %}
<li>
{% if af. website %}
    <a href="{{ af.website }}">
      {{ af.name }}
    </a>
{% else %}
	{{ af.name }}
{% endif %}
	</li>
{% endif %}	
{% endfor %}
</ul>

<h2>Alumni</h2>
[See the complete list here](documents/alumni.md).
