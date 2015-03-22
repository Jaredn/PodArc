# PodArc
Django web project to build medium to large scale (not super-scale) datacenter network architectures.  This database driven approach allows automation of device configurations, network topologies, and lends itself towards "SDN".  Workflow is as follows...:
<br/>

<h3>Build physical locations inside of the app</h3>
<div>
<ul>
<li>Create a "<b>Datacenter</b>" location</li>
<li>Create a "<b>Cage</b>" inside the "<b>datacenter</b>"</li>
<li>Create a "<b>Row</b>" inside of a "<b>Cage</b>"</li>
<li>Create a "<b>Rack</b>" inside of a "<b>Row</b>"</li>
</ul>
</div>

<h3>Create definitions of your network architecture building blocks, called "<b>Pods</b>"</h3>
<div>
<ul>
<li>Using <b>YAML</b>, define different <b>Pods</b>...</li>
<ul>
<li>Pair of large devices</li>
<li>4x16 CLOS fabrics</li>
<li>6 TORs in a full mesh</li>
<li>etc...</li>
</ul>
</ul>
</div>

<h3>Finally - Build your network</h3>
<div>
<ul>
	<li>Create a "<b>Pod</b>" inside of a "<b>Datacenter</b>"</li>
	<ul>
		<li>Ghost "<b>devices</b>" as defined by your "<b>pod definition</b>" now exist in your database</li>
		<li>All physical interconnections now exist inside of your database (to be used later for config generation)</li>
	</ul>
	<li>Assign system MACs to "<b>devices</b>" for use with Zero Touch Provisioning.</li>
	<ul>
		<li>Config Generation creates individual device base configs using Jinja2 templates</li>
		<li>Those config files get pushed to repository and host entries are added to DHCP server for ZTP requiring download of generated configuration</li>
	</ul>
	<li>Connect "<b>Pods</b>" to other "<b>Pods</b>" to create a large datacenter network</li>
	<ul>
		<li>Uses "<b>Pod Definition</b>" file which reserves "<b>network infrastructure</b>" ports for pod interconnection</li>
	</ul>
</ul>
</div>
