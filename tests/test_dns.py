
def test_srv():
    from plumb_util.dns_srv import find_service
    res = find_service('_ldap._tcp', zone='openldap.org')
    assert tuple(res[0]) == ('www.openldap.org.',389)

def test_txt():
    from plumb_util.dns_srv import find_text
    res = find_text('_kerberos', zone='lumino.so')
    assert res == 'LUMINOSO-LLC.COM'
