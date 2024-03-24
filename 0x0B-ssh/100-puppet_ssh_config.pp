#!/usr/bin/env bash
# Puppet manifest to configure SSH client settings
# Configure SSH client to use private key and disable password authentication
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
  content => "# SSH client configuration\n
              Host ubuntu\n
                  HostName 54.237.122.100\n
                  IdentityFile ~/.ssh/school\n
                  PreferredAuthentications publickey\n
                  PasswordAuthentication no\n",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}
