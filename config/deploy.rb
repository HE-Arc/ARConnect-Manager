# config valid for current version and patch releases of Capistrano
lock "~> 3.18.1"


set :application, "ARConnect-Manager"
set :repo_url, "https://github.com/HE-Arc/ARConnect-Manager.git"

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, "/var/www/my_app_name"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []

# TODO : append :linked_files, '.env'

# append :linked_files, "config/database.yml", 'config/master.key'

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "public/system", "vendor", "storage"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for local_user is ENV['USER']
# set :local_user, -> { `git config user.name`.chomp }

# Default value for keep_releases is 5
# set :keep_releases, 5

# Uncomment the following to require manually verifying the host key before first deploy.
# set :ssh_options, verify_host_key: :secure

# Créer un lien symbolique vers le fichier .env dans le répertoire current/backend
after 'deploy:symlink:release', 'deploy:create_env_symlink'
namespace :deploy do
    desc 'Create symlink for .env files'
    task :create_env_symlink do
      on roles(:app) do
        execute "ln -sf #{shared_path}/.env-api #{release_path}/api/.env"
        execute "ln -sf #{shared_path}/.env-frontend #{release_path}/frontend/.env"
      end
    end
  end
  
# Installer les dépendances Python
after 'deploy:updating', 'pip:install'
namespace :pip do
    desc 'Install'
    task :install do
        on roles([:app, :web]) do |h|
        execute "pip install -r #{release_path}/api/requirements.txt"

        end
    end
end



# Construire et déployer l'application Vue.js
after 'deploy:updated', 'vue:deploy'
namespace :vue do
  desc 'Build and deploy Vue.js application'
  task :deploy do
    on roles(:app) do
      within release_path.join('frontend') do
        execute :npm, 'install' # Installer les dépendances npm
        execute :npm, 'run build' # Construire l'application Vue.js
      end
    end
  end
end

# Redémarrer le serveur Gunicorn
after 'deploy:publishing', 'gunicorn:restart'
namespace :gunicorn do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
        execute :sudo, 'systemctl restart gunicorn'
    end
    end
end
