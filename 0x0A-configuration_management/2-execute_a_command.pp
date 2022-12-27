# A manifest to kill a running process killmenow from the process table
# on every puppet run
exec { 'pkill -9 killmenow':
  path     => '/usr/bin:/bin',
  onlyif   => pgrep killmenow,
  provider => shell,

}
