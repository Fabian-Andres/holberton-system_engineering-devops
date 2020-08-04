#!/usr/bin/env bash
# kill me now
exec { 'kill killmenow process':
  command  => 'pkill killmenow',
  provider => 'shell',
}
