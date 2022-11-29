# Create Dictionary and List Objects
$dict = @{
    string_value = "text"
    int_value = 0
    bool_value = $true
}

$list = @(
    "string1"
    "string2"
    123456789
    987654321
    $true
    $false
)

# Create Credential
$username = "name"
$password = "password"
$cred = New-Object System.Management.Automation.PSCredential -ArgumentList ($username, (ConvertTo-SecureString $password -AsPlainText -Force))

# Get Current TimeStamp
$timestamp = (Get-Date).ToString('MM/dd/yyyy hh:mm:ss tt')

# Get Current Script Name
$name = $MyInvocation.MyCommand.Definition.Split('\')[-1].Split('.')[0]

# Enable TLS v1.2 for W2K8 support
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
[System.Net.ServicePointManager]::ServerCertifcateValidationCallBack = { $true }

# HTTP Get w/ Headers
function HTTP_Get_Headers($url) {
    try {
        $request = Invoke-WebRequest -Uri $url -Method GET -UserBasicParsing -Headers @{
            "Accept" = "application/json"
            "Authorization" = "SomeToken"
            "Content-Type" = "application/json"
        }
        return (request.Content | ConvertFrom-Json)
    }
    catch {
        Write-Error($_.Exception.Response.StatusDescription)
        Write-Error($_.Exception.Message)
    }
}

# HTTP Get w/ BasicAuth
function HTTP_Get_BasicAuth($url) {
    try {
        $request = Invoke-WebRequest -Uri $url -Method GET -UserBasicParsing -Credential $creds
        return (request.Content | ConvertFrom-Json)
    }
    catch {
        Write-Error($_.Exception.Response.StatusDescription)
        Write-Error($_.Exception.Message)
    }
}

$body = @{
    parameter1 = "text"
    parameter2 = "text"
}

# HTTP Post w/ Headers
function HTTP_Post_Headers($url, $body) {
    try {
        $request = Invoke-WebRequest -Uri $url -Method POST -UserBasicParsing -Body ($body | ConvertTo-Json) -Headers @{
            "Accept" = "application/json"
            "Authorization" = "SomeToken"
            "Content-Type" = "application/json"
        }
        return (request.Content | ConvertFrom-Json)
    }
    catch {
        Write-Error($_.Exception.Response.StatusDescription)
        Write-Error($_.Exception.Message)
    }
}

# HTTP Post w/ BasicAuth
function HTTP_Post_BasicAuth($url, $body) {
    try {
        $request = Invoke-WebRequest -Uri $url -Method POST -UserBasicParsing -Body ($body | ConvertTo-Json) -Credential $creds
        return (request.Content | ConvertFrom-Json)
    }
    catch {
        Write-Error($_.Exception.Response.StatusDescription)
        Write-Error($_.Exception.Message)
    }
}

# SQL Select
function SQL_SELECT($query) {
    # $Connection = New-Object System.Data.SqlClient.SqlConnection("Server=myDBServer; Database=myDatabase; User Id=someUser; Password=password;")
    $Connection = New-Object System.Data.SqlClient.SqlConnection("Server=myDBServer; Database=myDatabase; Integrated Security=TRUE;")
    $Command = New-Object System.Data.SqlClient.SqlCommand($query, $Connection)
    $Connection.Open()
    $Adapter = New-Object System.Data.SqlClient.SQLDataAdapter $Command
    $Data = New-Object System.Data.DataSet
    $Adapter.Fill($Data) | Out-Null
    $Connection.Close()
    return $Data.HasErrors ? $Data : $Data.Tables
}

# SQL Update
function SQL_UPDATE($query) {
    # $Connection = New-Object System.Data.SqlClient.SqlConnection("Server=myDBServer; Database=myDatabase; User Id=someUser; Password=password;")
    $Connection = New-Object System.Data.SqlClient.SqlConnection("Server=myDBServer; Database=myDatabase; Integrated Security=TRUE;")
    $Command = New-Object System.Data.SqlClient.SqlCommand($query, $Connection)
    $Connection.Open()
    $Result = $Command.ExecuteNonQuery()
    $Connection.Close()
    return $Result
}

# Run Commands on Remote Target
$Result = Invoke-Command -ComputerName "Name" -Credential $creds -ScriptBlock {
    Import-Module WebAdministration
    $WebSites = Get-ChildItem -Path IIS:\Sites
    New-Object -Type PSObject -Prop $WebSites # This makes data available to main script
}
 Write-Host $Result.WebSites
