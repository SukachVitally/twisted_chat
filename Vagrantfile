# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "bento/centos-7.1"

  config.berkshelf.enabled = true
  config.berkshelf.berksfile_path = "./cookbooks/twistedchat/Berksfile"
  config.vm.provision "chef_solo" do |chef|
    chef.add_recipe "twistedchat"
    chef.add_recipe "twistedchat::develop"
  end

  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 80, host: 8080
end
