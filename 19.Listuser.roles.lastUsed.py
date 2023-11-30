import boto3

def get_iam_roles_with_last_used():
    # Create an IAM client
    iam = boto3.client('iam')

    # List all IAM roles
    roles = iam.list_roles()['Roles']

    # Iterate through each role and get last used information
    for role in roles:
        role_name = role['RoleName']

        # Get the role details
        role_details = iam.get_role(RoleName=role_name)['Role']

        # Get the last used information for the role
        try:
            last_used = iam.get_role_last_used(RoleName=role_name)['RoleLastUsed']
            last_used_date = last_used.get('LastUsedDate', 'N/A')
            print(f"Role: {role_name}, Last Used Date: {last_used_date}")
        except iam.exceptions.RoleLastUsedNotFoundException:
            # If the role has not been used, handle the exception
            print(f"Role: {role_name}, Last Used Date: Never")

if __name__ == '__main__':
    get_iam_roles_with_last_used()