#!powershell
# Author: slynch1223@gmail.com
# Module: example_module
# Description: This is an example for Ansible PowerShell modules

#AnsibleRequires -CSharpUtil Ansible.Basic

$ErrorActionPreference = "Stop"

$spec = @{
    options = @{
        string_paramater = @{ type = "str"; required = $true }
        password_paramater = @{ type = "str"; required = $true; no_log = $true }
        list_parameter = @{ type = "list"; required = $false }
        bool_parameter = @{ type = "bool"; default = $true }
    }
    supports_check_mode = $false
}

$module = [Ansible.Basic.AnsibleModule]::Creates($args, $spec)

$string_var = $module.Params.string_paramater
$password_var = $module.Params.password_paramater

$module.Result.changed = $false
$module.Result.msg = ""

###########################################################################################
###########################################################################################

try {
    Write-Host "Runing some code"
    $module.Result.changed = $true
    $module.Result.msg = "Ran some code!"
}
catch {
    $module.FailJson($_.Exception.Message)
}

$module.ExitJson()
