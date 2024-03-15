<!--
A JSP file that encapsulates database connections.

Public methods:
- public void getConnection() throws SQLException
- public void closeConnection() throws SQLException  
-->

<%@ page import="java.sql.*"%>

<%!
	// User id, password, and server information
	private String url = "jdbc:mysql://root:KyNadumruMMiWfyqTDlKxKAahdQRGoHR@monorail.proxy.rlwy.net:28119/railway:1433;DatabaseName=Ticket_Tech_database;TrustServerCertificate=True";
	private String uid = "root";
	private String pw = "KyNadumruMMiWfyqTDlKxKAahdQRGoHR";
	
	// Do not modify this url
	private String urlForLoadData = "mysql://root:KyNadumruMMiWfyqTDlKxKAahdQRGoHR@monorail.proxy.rlwy.net:28119/railway";
	
	// Connection
	private Connection con = null;
%>

<%!
	public void getConnection() throws SQLException 
	{
		try
		{	// Load driver class
			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		}
		catch (java.lang.ClassNotFoundException e)
		{
			throw new SQLException("ClassNotFoundException: " +e);
		}
	
		con = DriverManager.getConnection(url, uid, pw);
		Statement stmt = con.createStatement();
	}
   
	public void closeConnection() 
	{
		try {
			if (con != null)
				con.close();
			con = null;
		}
		catch (Exception e)
		{ }
	}
%>
