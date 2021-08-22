class PfSessionInfoFactory(object):

    @classmethod
    def get_pf_session_base_struct(cls):
        return {
            'user_id': None,
            'role': None,
            'student_number': None
        }