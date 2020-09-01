from datrics.services.storage_service import StorageService

# Routes
AUTH_SIGN_IN_ROUTE = 'auth/sign-in'
GET_PROJECTS_ROUTE = 'project'
PROJECT_BRICK_CREATE_ROUTE = 'project/:project_id/bricks'
PROJECT_BRICK_UPDATE_ROUTE = 'project/:project_id/bricks/:brick_id'
PROJECT_BRICK_DELETE_ROUTE = 'project/:project_id/bricks/:brick_id'

# URLs
PROD_BASE_API_URL = 'https://api.app.datrics.ai/api/v1'
saved_base_api_url = StorageService.get_api_base_url()
BASE_API_URL = PROD_BASE_API_URL if len(saved_base_api_url) == 0 else saved_base_api_url
# BASE_API_URL = 'http://localhost:3000/api/v1'
AUTH_SIGN_IN_URL = f'{BASE_API_URL}/{AUTH_SIGN_IN_ROUTE}'
GET_PROJECTS_URL = f'{BASE_API_URL}/{GET_PROJECTS_ROUTE}'
POST_PROJECT_BRICKS_URL = f'{BASE_API_URL}/{PROJECT_BRICK_CREATE_ROUTE}'
PATCH_PROJECT_BRICK_URL = f'{BASE_API_URL}/{PROJECT_BRICK_UPDATE_ROUTE}'
DELETE_PROJECT_BRICK_URL = f'{BASE_API_URL}/{PROJECT_BRICK_DELETE_ROUTE}'