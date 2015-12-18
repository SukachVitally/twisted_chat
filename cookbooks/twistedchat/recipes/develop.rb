home_dir = node[:home_dir]
dev_owner = node[:dev_owner]
venv_dir = node[:venv_dir]


execute 'venv init' do
  user dev_owner
  command "virtualenv #{venv_dir}"
  action :run
end
Chef::Log.warn("Virtualenv directory created")

template "/etc/nginx/nginx.conf" do
    source 'nginx.conf.erb'
    mode '0644'
end

service "nginx" do
  action :start
end
