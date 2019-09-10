Vagrant.configure(2) do |config|
  config.vm.hostname = "webhook" 
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "public_network"
  config.vm.synced_folder "/data/vagrant/python", "/vagrant_data"
  config.vm.provider 'virtualbox' do |vb|	
  # Display the VirtualBox GUI when booting the machine
    vb.gui = false
   # Customize the amount of memory on the VM:
    vb.memory = "1024"
  # Customize number of CPU's
    vb.cpus = "2"
   end
  #
   config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get update
  SHELL
end
