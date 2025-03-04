Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"  # Ubuntu 22.04 LTS (Jammy Jellyfish)
  config.vm.hostname = "vm-python-dev"  # Nombre de la máquina virtual

  config.vm.network "forwarded_port", guest: 80, host: 9090  # Redirección de puertos
  config.vm.network "forwarded_port", guest: 8000, host: 9000  # Redirección de Django a 9000 en el host
  config.vm.network "private_network", ip: "192.168.56.3"  # IP fija en red privada

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"  # Aumentamos la memoria a 4GB para mejor rendimiento
    vb.cpus = 4  # Usamos 4 núcleos
  end

  config.vm.provision "shell", inline: <<-SHELL
    # Actualización del sistema
    apt update && apt upgrade -y
    
    # Instalación de dependencias esenciales
    apt install -y python3 python3-pip python3-venv build-essential libssl-dev libffi-dev python3-dev
    
    # Configuración de Python
    pip3 install --upgrade pip
    python3 -m venv /home/vagrant/python_env
    source /home/vagrant/python_env/bin/activate
    pip install numpy pandas flask requests django
    
    # Iniciar un proyecto Django y ejecutar el servidor en el puerto 8000 dentro de la VM
    django-admin startproject myproject /home/vagrant/myproject
    cd /home/vagrant/myproject
    python manage.py runserver 0.0.0.0:8000 &
  SHELL
end
