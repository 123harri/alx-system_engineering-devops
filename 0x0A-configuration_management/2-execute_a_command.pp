# Description: This Puppet manifest kills a process named "killmenow" using pkill.

exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],  # Add additional paths if needed
  onlyif      => 'pgrep killmenow',
}
