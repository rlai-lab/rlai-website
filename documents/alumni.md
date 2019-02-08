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
 	<li><a href="http://webdocs.cs.ualberta.ca/~abbasiya/" target="_blank" rel="noopener noreferrer">Yasin Abbasi-Yadkori</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~afkanpou/" target="_blank" rel="noopener noreferrer">Arash Afkanpour</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~ozlem/" target="_blank" rel="noopener noreferrer">Oslem Aslan</a></li>
 	<li><a href="https://scholar.google.ca/citations?user=WpAH4iUAAAAJ&amp;hl=en">Bernardo Ávila Pires</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~gbalazs/" target="_blank" rel="noopener noreferrer">Gabor Balazs</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~nolan/" target="_blank" rel="noopener noreferrer">Nolan Bard</a></li>
 	<li><a href="http://www.ualberta.ca/~bartok/" target="_blank" rel="noopener noreferrer">Gabor Bartok</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~dwyer/" target="_blank" rel="noopener noreferrer">Ken Dwyer</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~farhang/" target="_blank" rel="noopener noreferrer">Alireza Farhangfar</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~mg17/" target="_blank" rel="noopener noreferrer">Marc Gendron-Bellemare</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~johanson/" target="_blank" rel="noopener noreferrer">Michael Johanson</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~lanctot/" target="_blank" rel="noopener noreferrer">Marc Lanctot</a></li>
 	<li><a href="https://webapps.cs.ualberta.ca/profile/?who=97322" target="_blank" rel="noopener noreferrer">Ashique Rupam Mahmood</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~neufeld/" target="_blank" rel="noopener noreferrer">James Neufeld</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~rayner/" target="_blank" rel="noopener noreferrer">Chris Rayner</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~ys3/" target="_blank" rel="noopener noreferrer">Yi Shi</a></li>
 	<li><a href="http://www.adamwhite.ca/" target="_blank" rel="noopener noreferrer">Adam White</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~whitem/" target="_blank" rel="noopener noreferrer">Martha White</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~myang2/" target="_blank" rel="noopener noreferrer">Min Yang</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~hengshua/" target="_blank" rel="noopener noreferrer">Hengshuai Yao</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~yaoliang/" target="_blank" rel="noopener noreferrer">Yaoliang Yu</a></li>
 	<li><a href="http://academic.sologen.net/Home.html" target="_blank" rel="noopener">Amir massoud Farahmand </a>(PhD, June 2011)</li>
 	<li><a href="http://www.cis.temple.edu/~yuhong">Yuhong Guo</a> (PhD, 2007)</li>
 	<li><a href="http://www-personal.umich.edu/~danjl">Dan Lizotte</a> (PhD, 2008)</li>
 	<li><a href="http://www.stanford.edu/~maei/" target="_blank" rel="noopener">Hamid Maei</a> (PhD, 2011)</li>
 	<li><a href="http://sites.google.com/site/qiniriswang">Qin Iris Wang</a> (PhD, 2008)</li>
 	<li><a href="http://www.cs.purdue.edu/~taowang">Tao Wang</a> (PhD, 2007)</li>
</ul>
<h2>M.Sc. Students</h2>
<ul>
 	<li><a href="http://www.michaeljoya.com" target="_blank" rel="noopener noreferrer">Michael Joya</a></li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~delp/" target="_blank" rel="noopener">Michael Delp</a> (MSc, 2010)<a href="http://webdocs.cs.ualberta.ca/~delp/" target="_blank" rel="noopener">
</a></li>
 	<li>Neda Mirian (MSc, 2011)<a href="http://webdocs.cs.ualberta.ca/~mirianho/" target="_blank" rel="noopener">
</a></li>
 	<li><a href="http://research.tannerpages.com/" target="_blank" rel="noopener">Brian Tanner
</a></li>
 	<li><a href="http://www.cs.cmu.edu/~kwaugh">Kevin Waugh</a> (MSc, 2009)</li>
 	<li><a href="http://webdocs.cs.ualberta.ca/~hackman/">Leah Hackman </a>(MSc, 2012)</li>
 	<li><a href="https://plus.google.com/+TravisDickTheLearner/posts">Travis Dick </a></li>
</ul>
