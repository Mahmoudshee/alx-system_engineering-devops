# Puppet manifest to change OS configuration for the holberton user

# Define the exec resource to change the ulimit for the holberton user
exec { 'change-os-configuration-for-holberton-user':
  command  => 'ulimit -n 1024',
  user     => 'root',
  creates  => '/tmp/holberton_configuration_changed',
  require  => File['/etc/security/limits.conf'],
}

# Ensure the limits.conf file exists
file { '/etc/security/limits.conf':
  ensure => present,
}

# Define the limits for the holberton user in the limits.conf file
file_line { 'holberton_limits':
  path    => '/etc/security/limits.conf',
  line    => 'holberton hard nofile 1024',
  require => File['/etc/security/limits.conf'],
}

