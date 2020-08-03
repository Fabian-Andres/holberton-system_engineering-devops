#!/usr/bin/env bash
# Create a file using puppet
file { '/tmp/holberton':
    ensure  => present,
    path    => '/tmp/holberton',
    content => "I love Puppet\n",
    group   => 'www-data',
    mode    => '0744',
    owner   => 'www-data',
}
