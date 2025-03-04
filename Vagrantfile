Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"  # Ubuntu 22.04 LTS
  config.vm.hostname = "vm-python-mysql"  # Nombre de la VM

  # Redirección de puertos
  config.vm.network "forwarded_port", guest: 80, host: 9090   # Web
  config.vm.network "forwarded_port", guest: 8000, host: 9000 # Django
  config.vm.network "forwarded_port", guest: 3306, host: 33060 # MySQL
  config.vm.network "private_network", ip: "192.168.56.3"     # IP fija

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"  # RAM: 4GB
    vb.cpus = 4         # Núcleos: 4
  end

  config.vm.provision "shell", inline: <<-SHELL
    # Actualización del sistema
    apt update && apt upgrade -y

    # Instalación de dependencias esenciales
    apt install -y python3 python3-pip python3-venv build-essential libssl-dev libffi-dev python3-dev

    # Instalación de MySQL Server
    apt install -y mysql-server
    systemctl enable mysql
    systemctl start mysql

    # Configurar MySQL para permitir conexiones remotas
    sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf
    systemctl restart mysql

    # Crear usuario root con acceso remoto
    mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';"
    mysql -e "CREATE USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';"
    mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;"
    mysql -e "FLUSH PRIVILEGES;"

    # Configuración de Python
    pip3 install --upgrade pip
    python3 -m venv /home/vagrant/python_env
    source /home/vagrant/python_env/bin/activate
    pip install numpy pandas flask requests django mysql-connector-python

    # Crear proyecto Django con MySQL
    django-admin startproject myproject /home/vagrant/myproject
    cd /home/vagrant/myproject
    python manage.py runserver 0.0.0.0:8000 &
  SHELL
end
