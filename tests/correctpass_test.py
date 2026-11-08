import pytest
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

class TestUserProfile:
    def test_password_user_profile(self):
        valid = ["sEcure123!", "Password1@", "A1@bcdefg"]
        invalid = ["weak", "password123", "Password"]
        for pas in valid:
            assert UserProfile.valid_password(pas)
        for pas in invalid:
            assert not UserProfile.valid_password(pas)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
