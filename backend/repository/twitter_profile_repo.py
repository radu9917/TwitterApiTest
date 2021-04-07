from repository.repo_interface import IRepo
import copy


class TwitterProfileRepo(IRepo):
    def __init__(self):
        self.profile_list = []
        self.id = 1

    def store(self, profile):
        if profile.get_profile_id() == 0:
            profile.set_profile_id(self.id)
            self.id += 1
        self.profile_list.append(copy.deepcopy(profile))

    def delete(self, profile_id):
        for profile in self.profile_list:
            if profile_id == profile.get_profile_id():
                self.profile_list.remove(profile)

    def update(self, old_profile_id, new_profile):
        for profile in self.profile_list:
            if old_profile_id == profile.get_profile_id():
                new_profile.set_profile_id(old_profile_id)
                self.delete(old_profile_id)
                self.store(new_profile)

    def get_all(self):
        return copy.deepcopy(self.profile_list)

    def get(self, profile_id):
        for profile in self.profile_list:
            if profile_id == profile.get_profile_id():
                return copy.deepcopy(profile)
