
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

public class MyConn {
    public static void main(String[] args) throws ClassNotFoundException {
     Connection connect = null;
     Statement stm = null;
     String host = "192.168.66.200";
     String DB = "asterisk";
     try{
         Class.forName("com.mysql.jdbc.Driver");
         connect = DriverManager.getConnection("jdbc:mysql://" + host + "/asterisk" + "?user=dcall&password=dcallpass");
         stm = connect.createStatement();
         String sql = "SELECT trunks.trunkid, trunks.name, trunks.outcid FROM trunks\n" +
                      "INNER JOIN outbound_route_trunks ON trunks.trunkid = outbound_route_trunks.trunk_id";
         ResultSet rec = stm.executeQuery(sql);
         
         while((rec != null) && (rec.next())){
             System.out.print("TrunkName:" + rec.getString("name") + " | OutCID:" + rec.getString("outcid"));
             //System.out.print(rec.getString("outcid") + " | ");
             //System.out.print(rec.getString("match_cid"));
             System.out.println("");        
         }
        
     }catch(Exception e){
         e.printStackTrace();
     }
     
     try{
         if(connect != null)
             connect.close();
     
     }catch(SQLException e){
         e.printStackTrace();
     }
    }
    
}