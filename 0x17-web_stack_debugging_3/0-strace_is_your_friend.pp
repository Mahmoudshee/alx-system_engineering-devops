exec { 'fix_apache':
  command => 'sed -i "s/^\tLogLevel.*/\tLogLevel info/g" /etc/apache2/apache2.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

