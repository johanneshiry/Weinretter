
def import_rconfig
    require 'yaml'
    current_dir    = File.dirname(File.expand_path(__FILE__))

    begin
        YAML.load_file("#{current_dir}/dev/config.local.yml")
    rescue
        YAML.load_file("#{current_dir}/dev/config.yml")
    end
end

rconfig = import_rconfig

Vagrant.configure("2") do |config|
    if rconfig['provider'] == 'libvirt'
        config.vm.provider "libvirt"
    else
        config.vm.provider "virtualbox"
    end


    config.vm.box = "debian/buster64"

    if rconfig['provider'] == 'libvirt'
        config.vm.provider :libvirt do |lv|
            lv.memory = rconfig['ram']
            lv.cpus = rconfig['cpu']
        end
    else
        config.vm.provider :virtualbox do |vb|
            vb.memory = rconfig['ram']
            vb.cpus = rconfig['cpu']
            vb.customize [
                                    "modifyvm", :id,
                                    "--memory", '%d' % [rconfig['ram']]
                                  ]
        end
    end

    config.vm.provision "docker" do |d|
        d.pull_images "hello-world" # dummy command (to install docker)
    end


    config.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "/vagrant/dev/playbook.yml"
        ansible.verbose        = true
        ansible.limit          = "all"
        ansible.inventory_path = "/vagrant/dev/hosts"
        #ansible.verbose        = "vvv"
        ansible.install_mode	 = "pip"
        #ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }

        ansible.extra_vars = {
            in_vagrant: true
        }
    end
end