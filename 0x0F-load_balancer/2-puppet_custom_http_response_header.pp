# File: 2-puppet_custom_http_response_header.pp

# Update system
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install Nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Create index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Add redirect rule
exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Add custom HTTP header
exec { 'HTTP header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
