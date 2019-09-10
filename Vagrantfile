Vagrant.configure(2) do |config|
  config.vm.hostname = "SampleTest"
  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder "/home/devops/vagrant_share/example01" , "/data"
  config.vm.network :forwarded_port, guest:80 , host:8000
  config.vm.provider 'virtualbox' do |vb|
    vb.gui = false
    vb.memory= "1024"
    vb.cpus = "2"
  end
end
