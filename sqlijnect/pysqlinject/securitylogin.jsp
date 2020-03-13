<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*"%>

<html>
<head>
    <title>登录</title>
</head>
    <body>
    <%  
        String name = request.getParameter("username");
        String pwd = request.getParameter("password");
                	String drivername="com.microsoft.jdbc.sqlserver.SQLServerDriver";	
	String uname="sqlinjection";	
	String userpassword="sql";	
	String dbname="pysqlinject";	
	String url = "jdbc:microsoft:sqlserver://127.0.0.1:1433;DatabaseName="+dbname;
        try {  
          	Class.forName(drivername).newInstance();
	          Connection conn=DriverManager.getConnection(url,uname, userpassword);	

            if(conn != null){            
                String sql = "SELECT id from userinfo where name1 = ? and passwd = ?";  //查询语句
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setString(1,name);
                pstmt.setString(2,pwd);
                ResultSet rs = pstmt.executeQuery();
                if(rs.next()) {  
                    pageContext.forward("success.jsp"); 
                } 
                else{
                    pageContext.forward("fail.jsp");
                }
            }
            else
                out.print("连接失败！");   
        }catch (Exception e) {        
            out.print("数据库连接异常！");  
        }  
    %>   
    </body>
</html>

