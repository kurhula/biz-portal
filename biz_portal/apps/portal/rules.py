import logging

import rules

logger = logging.getLogger(__name__)


@rules.predicate
def is_business_muni_admin(user, business):
    if business is None:
        return True
    logger.debug("### rules is_business_muni_admin {user} {business}")
    return (
        user.is_staff
        and user.municipality_set.filter(pk=business.region.municipality.pk).exists()
    )


@rules.predicate
def is_muni_admin(user):
    logger.debug("### rules is_muni_admin")
    return user.is_staff and user.municipality_set.exists()


rules.add_perm("portal", rules.always_allow)
rules.add_perm("portal.view_business", rules.always_allow)
rules.add_perm("portal.add_business", is_muni_admin)
rules.add_perm("portal.change_business", is_business_muni_admin)
rules.add_perm("portal.delete_business", is_business_muni_admin)
