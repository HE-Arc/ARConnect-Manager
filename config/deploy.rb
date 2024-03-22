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

namespace :deploy do
  desc 'Create symlink for .env file'
  task :create_env_symlink do
    on roles(:app) do
      execute "ln -sf #{shared_path}/.env #{release_path}/api/.env"
    end
  end

  desc 'Migrate database'
  task :migrate_database do
    on roles(:app) do
      within release_path.join('api') do
        execute :python, 'manage.py migrate'
      end
    end
  end

  desc 'Collect static files'
  task :collect_static do
    on roles(:app) do
      within release_path.join('api') do
        execute :python, 'manage.py collectstatic --noinput'
      end
    end
  end
end

namespace :pip do
  desc 'Install'
  task :install do
      on roles([:app, :web]) do |h|
      execute "pip install -r #{release_path}/api/requirements.txt"
      end
  end
end

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

namespace :gunicorn do
desc 'Stop application'
task :stop do
  on roles(:app) do
    execute :sudo, 'systemctl stop gunicorn'
  end
end

desc 'Restart application'
task :restart do
  on roles(:app) do
    execute :sudo, 'systemctl restart gunicorn'
  end
end
end

# Créer un lien symbolique vers le fichier .env dans le répertoire current/backend
after 'deploy:symlink:release', 'deploy:create_env_symlink'

# Installer les dépendances Python
after 'deploy:updating', 'pip:install'

# Construire et déployer l'application Vue.js
after 'deploy:updated', 'vue:deploy'

# Redémarrer le serveur Gunicorn
after 'deploy:publishing', 'gunicorn:stop'
after 'gunicorn:stop', 'gunicorn:restart'

# Après le redémarrage de Gunicorn, exécutez les migrations de la base de données et collectez les fichiers statiques
after 'gunicorn:restart', 'deploy:migrate_database'
after 'gunicorn:restart', 'deploy:collect_static'