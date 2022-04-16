from typing import List
from src.main.common.constants import Environment
import git
import os
import threading
import re


class MGit(object):

    def __init__(self):
        self.current_dir = './'
        self.dirs = self._get_curdir()
        print(self.dirs)

    def _get_curdir(self) -> List:
        items = os.listdir(self.current_dir)
        dirs = [_ for _ in items if _ is not os.path.isdir(_)]
        removal_list = []
        for dir in dirs:
            if dir.startswith('.'):
                removal_list.append(dir)
                continue
            try:
                git.Repo(self.current_dir + dir)
            except Exception:
                removal_list.append(dir)
                continue
        return [_ for _ in dirs if _ not in removal_list]

    def sync(self) -> None:
        def _sync(_repo: git.Repo):
            semaphore.acquire()
            _repo.git.fetch(**{"all": True, "prune": True, "tags": True, "force": True})
            _repo.git.checkout('master')
            _repo.git.pull()
            semaphore.release()

        semaphore = threading.Semaphore()
        for dir in self.dirs:
            print(f'Syncing {dir} ...')
            repo = git.Repo(self.current_dir + dir)
            thread = threading.Thread(target=_sync, args=(repo,))
            thread.start()
        while threading.active_count() != 1:
            pass
        else:
            print('Completed Syncing.')

    def commit(self, image_tag: str, environment: str) -> None:
        def _commit(_repo: git.Repo, _image_tag: str, _environment, _commit_file: str):
            semaphore.acquire()
            _repo.git.checkout('HEAD')
            _repo.index.add(_commit_file)
            _repo.index.commit(f'Deploy MS {_image_tag} to {_environment}')
            semaphore.release()

        semaphore = threading.Semaphore()
        for dir in self.dirs:
            filename = f'{self.current_dir}{dir}/overlays/{environment}/base/kustomization.yaml'
            print(filename)
            commit_file = [f'overlays/{environment}/base/kustomization.yaml']
            print(f'Committing {dir} ...')
            with open(filename, mode='r', encoding='utf-8') as f:
                content = f.read()
            with open(filename, mode='w', encoding='utf-8') as f:
                content = re.sub('newTag:.+', f'newTag: {image_tag}', content)
                print(content)
                f.write(content)
            repo = git.Repo(self.current_dir + dir)
            thread = threading.Thread(target=_commit, args=(repo, image_tag, environment, commit_file))
            thread.start()
        while threading.active_count() != 1:
            pass
        else:
            print('Completed Committing.')

    def push(self) -> None:
        def _push(_repo: git.Repo):
            semaphore.acquire()
            _repo.git.checkout('HEAD')
            _repo.git.push()
            semaphore.release()

        semaphore = threading.Semaphore()
        for dir in self.dirs:
            print(f'Pushing {dir} ...')
            repo = git.Repo(self.current_dir + dir)
            thread = threading.Thread(target=_push, args=(repo,))
            thread.start()
        while threading.active_count() != 1:
            pass
        else:
            print('Completed Pushing.')

