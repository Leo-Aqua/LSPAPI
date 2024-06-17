from LSP import LSPAPI

user = ""  # LSP username
password = ""  # LSP password

key_file = "keyfile.key"  # The file where cookies are saved (for fater second login)
key_file_password = "supersecretpassword"  # encryption password for keyfile

lsp_api = LSPAPI(user, password, key_file, key_file_password)
lsp_api.start()
try:
    # All functions
    print(lsp_api.vehicle_states())
    print(lsp_api.user_stats())
    print(lsp_api.vehicles())
    print(lsp_api.buildings())

finally:
    lsp_api.stop()
